"""
Analytics Agent.
"""

from agents.base.state import AgentState
from tools.analytics.analytics_tool import AnalyticsTool


class AnalyticsAgent:

    def __init__(self):

        self.analytics_tool = AnalyticsTool()

    def invoke(self, state: AgentState) -> AgentState:
        print("\n========== ANALYTICS AGENT ==========")
        # print(f"Consulta : {state.user_query}")
        state.current_agent = "Analytics Agent"

        return self.analytics_tool.invoke(state)