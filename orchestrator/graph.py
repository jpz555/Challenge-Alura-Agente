"""
orchestrator/graph.py

Construcción del grafo principal del sistema multiagente.
"""

from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph
from agents.base.state import AgentState
from orchestrator.nodes import supervisor_node,knowledge_node, analytics_node, decision_node
from orchestrator.graph_router import GraphRouter

from IPython.display import Image
from IPython.display import display
from pathlib import Path

class AgentGraph:
    """
    Grafo principal del sistema.
    """

    def __init__(self):
        
        self.builder = StateGraph(AgentState)
        self._build()
        self.graph = self.builder.compile()

    def _build(self):
        # Nodos
        self.builder.add_node("supervisor",supervisor_node)
        self.builder.add_node("knowledge",knowledge_node)
        # Placeholders (por ahora)
        self.builder.add_node("analytics", analytics_node)
        self.builder.add_node("decision", decision_node)

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