"""
Analytics Agent.

Responsabilidades
-----------------
- Recibir consultas analíticas.
- Delegar la ejecución a AnalyticsTool.
- Actualizar el AgentState.
"""

from agents.base.base_agent import BaseAgent
from agents.base.state import AgentState

from tools.analytics.analytics_tool import AnalyticsTool
from tools.rag.rag_tool import RAGTool


class AnalyticsAgent(BaseAgent):
    def __init__(self, rag_tool: RAGTool):

        super().__init__("Analytics Agent")
        
        print("[AnalyticsAgent] Inicializando LLM...")
        self.analytics_tool = AnalyticsTool()

    # Invoke
    def invoke(self, state: AgentState) -> AgentState:

        print("\n========== ANALYTICS AGENT ==========")
        # print(f"Pregunta : {state.user_query}")
        state.current_agent = self.name
        return self.analytics_tool.invoke(state)