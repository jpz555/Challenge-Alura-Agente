"""
Scheduling Tool.
"""

from langchain_core.tools import tool

from tools.base.base_tool import BaseTool


class SchedulingTool(BaseTool):

    name = "Scheduling Tool"

    description = "Herramientas para programación."

    @tool
    def optimize_schedule(problem: str):
        """Optimiza programación."""
        pass

    @tool
    def allocate_resources(problem: str):
        """Asigna recursos."""
        pass

    @tool
    def balance_workload(problem: str):
        """Balancea carga de trabajo."""
        pass

    def get_tools(self):

        return [
            self.optimize_schedule,
            self.allocate_resources,
            self.balance_workload,
        ]