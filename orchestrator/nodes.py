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


# modelos llm
model = ModelFactory.create(provider='groq')

# data
data = CorporateDataLoader(Path("documents/data/corporate_data.xlsx"))


# Agentes
# componentes compartidos
rag_tool = RAGTool()
supervisor = SupervisorAgent(model=model)
knowledge = KnowledgeAgent(rag_tool=rag_tool)
analytics = AnalyticsAgent(rag_tool=rag_tool, model=model, corporate_data=data)
decision_support = DecisionSupportAgent(rag_tool=rag_tool, model=model)

def supervisor_node(state: AgentState) -> AgentState:
    """
    Nodo Supervisor.
    """
    # print(type(state))
    # print(state)
    return supervisor.invoke(state)


def knowledge_node(state: AgentState) -> AgentState:
    """
    Nodo Knowledge.
    """
    return knowledge.invoke(state)

def analytics_node(state: AgentState) -> AgentState:
    """
    Nodo Analytics.
    """
    return analytics.invoke(state)
    

def decision_node(state: AgentState) -> AgentState:
    """
    Nodo Decision Support.
    """
    # state.response = "Decision Support Agent aún no implementado."
    return decision_support.invoke(state)