"""
orchestrator/nodes.py

Nodos del grafo de LangGraph.
"""

from pathlib import Path

from agents.base.state import AgentState

from agents.supervisor.supervisor_agent import SupervisorAgent
from agents.knowledge.knowledge_agent import KnowledgeAgent
from agents.analytics.analytics_agent import AnalyticsAgent
from agents.decision_support.decision_support_agent import DecisionSupportAgent
from rag.models import ModelFactory
from tools.data.corporate_data_loader import CorporateDataLoader
from tools.rag.rag_tool import RAGTool




class GraphNodes:
    def __init__(self, provider=None, model=None):
        # modelos llm
        llm = ModelFactory.create(provider=provider, model=model)
        # data
        data = CorporateDataLoader(Path("documents/data/corporate_data.xlsx"))
        
        # Agentes
        # componentes compartidos
        rag_tool = RAGTool()
        self.supervisor = SupervisorAgent(model=llm)
        self.knowledge = KnowledgeAgent(rag_tool=rag_tool)
        self.analytics = AnalyticsAgent(rag_tool=rag_tool, model=llm, corporate_data=data)
        self.decision_support = DecisionSupportAgent(rag_tool=rag_tool, model=llm)

    def supervisor_node(self, state: AgentState) -> AgentState:
        """
        Nodo Supervisor.
        """
        # print(type(state))
        # print(state)
        return self.supervisor.invoke(state)


    def knowledge_node(self, state: AgentState) -> AgentState:
        """
        Nodo Knowledge.
        """
        return self.knowledge.invoke(state)

    def analytics_node(self, state: AgentState) -> AgentState:
        """
        Nodo Analytics.
        """
        return self.analytics.invoke(state)
        

    def decision_node(self, state: AgentState) -> AgentState:
        """
        Nodo Decision Support.
        """
        # state.response = "Decision Support Agent aún no implementado."
        return self.decision_support.invoke(state)