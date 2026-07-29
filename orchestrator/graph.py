"""
orchestrator/graph.py

Construcción del grafo principal del sistema multiagente.
"""

from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph
from agents.base.state import AgentState
from orchestrator.nodes import GraphNodes
from orchestrator.graph_router import GraphRouter

from IPython.display import Image
from IPython.display import display
from pathlib import Path

from rag.models import ModelFactory
from tools.data.corporate_data_loader import CorporateDataLoader




class AgentGraph:
    """
    Grafo principal del sistema.
    """

    def __init__(self, nodes: GraphNodes):
        
        self.nodes = nodes
        self.builder = StateGraph(AgentState)
        self._build()
        self.graph = self.builder.compile()

    def _build(self):
        # Nodos
        self.builder.add_node("supervisor", self.nodes.supervisor.invoke)
        self.builder.add_node("knowledge",self.nodes.knowledge.invoke)
        # Placeholders (por ahora)
        self.builder.add_node("analytics", self.nodes.analytics.invoke)
        self.builder.add_node("decision", self.nodes.decision_support.invoke)

        # Inicio
        self.builder.add_edge(START,"supervisor")


        # Routing
        self.builder.add_conditional_edges("supervisor",
            GraphRouter.route,
            {
                "knowledge": "knowledge",
                "analytics": "analytics",
                "decision": "decision",
            }
        )

        # Final
        self.builder.add_edge("knowledge", END)
        self.builder.add_edge("analytics", END)
        self.builder.add_edge("decision", END)
        
    def visualize(self):
        """
        Visualiza el grafico de Langgraph.
        """
        display(Image(self.graph.get_graph().draw_mermaid_png()))
        
    
    def save_graph(self, filename: str = "agent_graph.png"):
        
        png = self.graph.get_graph().draw_mermaid_png()
        Path(filename).write_bytes(png)
        
        print(f"Grafo guardado en: {filename}")
        
    def mermaid(self):
        return self.graph.get_graph().draw_mermaid()

    def invoke(self, state: AgentState):
        print("\n========== AGENT GRAPH ==========")
        # print(type(state))
        # print(state)
        result = self.graph.invoke(state)
        return AgentState.model_validate(result)