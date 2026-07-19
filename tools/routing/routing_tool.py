"""
Routing Tool.
"""



from langchain_core.tools import tool

from tools.base.base_tool import BaseTool


class RoutingTool(BaseTool):

    name = "Routing Tool"

    description = ("Herramientas para optimización de rutas de transporte.")

    # ==========================================================
    # MODELOS
    # ==========================================================

    def optimize_routes(self, problem: dict):

        """
        Aquí irá la lógica para decidir
        qué modelo matemático utilizar.
        """

        raise NotImplementedError

    def estimate_delivery_time(self, problem: dict):

        raise NotImplementedError

    def calculate_route_cost(self, problem: dict):

        raise NotImplementedError

    # ==========================================================
    # TOOLS
    # ==========================================================

    @tool
    def optimize_routes_tool(problem: dict):
        """
        Optimiza rutas de distribución.
        """
        pass

    @tool
    def estimate_delivery_time_tool(problem: dict):
        """
        Estima tiempos de entrega.
        """
        pass

    @tool
    def calculate_route_cost_tool(problem: dict):
        """
        Calcula el costo de una ruta.
        """
        pass
    

    def get_tools(self):

        return [
            self.optimize_routes_tool,
            self.estimate_delivery_time_tool,
            self.calculate_route_cost_tool,
        ]