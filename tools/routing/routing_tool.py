"""
Funciones Tool para Routing.
"""

from langchain_core.tools import tool

from tools.routing.routing_engine import RoutingEngine


@tool
def optimize_routes_tool(problem: str, context: str) -> dict:
    """
    Optimiza las rutas de distribución.

    Úsala SOLO cuando el usuario solicite:
    - Optimizar rutas de entrega.
    - Encontrar la mejor ruta para distribuir pedidos.
    - Minimizar la distancia recorrida.
    - Reducir el costo de transporte mediante optimización de rutas.
    - Resolver un problema de ruteo de vehículos (VRP).

    NO la uses para:
    - Consultar tiempos estimados de entrega.
    - Calcular costos de transporte.
    - Consultar inventarios.
    - Programar recursos.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("optimize_routes_tool")
    print("Problema:", problem)
    
    engine = RoutingEngine()
    
    result_problem = engine.optimize_routes(problem=problem, context=context)

    return result_problem


@tool
def estimate_delivery_time_tool(problem: str) -> str:
    """
    Estima el tiempo de entrega de una ruta o pedido.

    Úsala SOLO cuando el usuario pregunte por:
    - Tiempo estimado de llegada.
    - Tiempo de entrega.
    - Duración aproximada de una ruta.
    - ETA de un vehículo.

    NO la uses para:
    - Optimizar rutas.
    - Calcular costos.
    - Consultar inventarios.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("estimate_delivery_time_tool")
    print("Problema:", problem)

    return f"Tiempo estimado calculado para: {problem}"


@tool
def calculate_route_cost_tool(problem: str) -> str:
    """
    Calcula el costo asociado a una ruta de transporte.

    Úsala SOLO cuando el usuario pregunte por:
    - Costo de una ruta.
    - Costo de transporte.
    - Gasto de distribución.
    - Comparación de costos logísticos.

    NO la uses para:
    - Optimizar rutas.
    - Estimar tiempos.
    - Consultar inventarios.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("calculate_route_cost_tool")
    print("Problema:", problem)

    return f"Costo de ruta calculado para: {problem}"