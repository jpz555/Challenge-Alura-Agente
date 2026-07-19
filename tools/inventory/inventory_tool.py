"""
Inventory Tool.
"""

from langchain_core.tools import tool

from tools.base.base_tool import BaseTool


class InventoryTool(BaseTool):

    name = "Inventory Tool"

    description = "Herramientas para optimización de inventarios."

    @tool
    def optimize_inventory(problem: str):
        """Optimiza inventarios."""
        pass

    @tool
    def calculate_reorder_point(problem: str):
        """Calcula punto de reorden."""
        pass

    @tool
    def classify_inventory(problem: str):
        """Clasificación ABC."""
        pass

    def get_tools(self):

        return [
            self.optimize_inventory,
            self.calculate_reorder_point,
            self.classify_inventory,
        ]