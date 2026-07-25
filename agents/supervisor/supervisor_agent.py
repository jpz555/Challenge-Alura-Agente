"""
agents/supervisor/agent.py

Supervisor del sistema multiagente.

Su única responsabilidad es analizar la consulta del usuario
y determinar qué agente debe atenderla.
"""

from agents.base.base_agent import BaseAgent
from agents.base.state import AgentState
from agents.supervisor.agent_router import SupervisorRouter
from rag.models import ModelFactory

class SupervisorAgent(BaseAgent):
    """
    Agente Supervisor.

    Analiza la consulta del usuario y determina
    qué agente debe ejecutarse.
    """

    def __init__(self, model: ModelFactory):
        super().__init__(name="Supervisor")

        self.router = SupervisorRouter(model)

    def invoke(self, state: AgentState) -> AgentState:

        print("\n========== SUPERVISOR ==========")
        # print(f"Pregunta : {state.user_query}")
        # print(f"Intent   : {state.intent}")
        state.intent = self.router.classify(state.user_query)

        return state