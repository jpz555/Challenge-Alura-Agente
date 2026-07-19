"""
Decision Support Agent.
"""

from agents.base.state import AgentState

from tools.routing.routing_tool import RoutingTool
from tools.inventory.inventory_tool import InventoryTool
from tools.scheduling.scheduling_tool import SchedulingTool


class DecisionSupportAgent:

    def __init__(self):

        self.routing_tool = RoutingTool()
        self.inventory_tool = InventoryTool()
        self.scheduling_tool = SchedulingTool()

    def invoke(self, state: AgentState) -> AgentState:
        print("\n========== DECISION SUPPORT ==========")
        # print(f"Consulta : {state.user_query}")
        state.current_agent = "Decision Support Agent"

        # En la siguiente fase clasificaremos
        # cuál herramienta ejecutar.
        return state