"""
Funciones Tool para Inventory.
"""

from langchain_core.tools import tool


@tool
def check_stock_tool(problem: str) -> str:
    """
    Consulta el nivel de stock o existencias de un producto.

    Úsala SOLO cuando el usuario pregunte por:
    - Stock disponible.
    - Existencias actuales.
    - Disponibilidad de un producto.
    - Cantidad disponible en inventario.

    NO la uses para:
    - Pronósticos de demanda.
    - Puntos de reorden.
    - Cantidad económica de pedido.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("check_stock_tool")
    print("Problema:", problem)

    return f"Consulta de stock ejecutada para: {problem}"


@tool
def forecast_demand_tool(problem: str) -> str:
    """
    Estima la demanda futura de un producto.

    Úsala SOLO cuando el usuario pregunte por:
    - Pronóstico de demanda.
    - Proyección de ventas.
    - Demanda futura.
    - Planeación de compras.

    NO la uses para:
    - Consultar stock actual.
    - EOQ.
    - Clasificación ABC.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("forecast_demand_tool")
    print("Problema:", problem)

    return f"Pronóstico de demanda calculado para: {problem}"


@tool
def reorder_point_tool(problem: str) -> str:
    """
    Calcula el punto de reorden de un producto.

    Úsala SOLO cuando el usuario pregunte por:
    - Punto de reorden.
    - Cuándo volver a comprar.
    - Nivel mínimo para reabastecer.
    - Momento de realizar un nuevo pedido.

    NO la uses para:
    - Pronóstico de demanda.
    - EOQ.
    - Consulta de stock.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("reorder_point_tool")
    print("Problema:", problem)

    return f"Punto de reorden calculado para: {problem}"


@tool
def calculate_safety_stock_tool(problem: str) -> str:
    """
    Calcula el inventario o stock de seguridad.

    Úsala SOLO cuando el usuario pregunte por:
    - Stock de seguridad.
    - Inventario de seguridad.
    - Nivel de protección ante variabilidad.
    - Buffer de inventario.

    NO la uses para:
    - Consultar stock actual.
    - EOQ.
    - Clasificación ABC.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("calculate_safety_stock_tool")
    print("Problema:", problem)

    return f"Stock de seguridad calculado para: {problem}"


@tool
def classify_inventory_abc_tool(problem: str) -> str:
    """
    Clasifica productos utilizando el método ABC.

    Úsala SOLO cuando el usuario pregunte por:
    - Clasificación ABC.
    - Clasificación de inventarios.
    - Productos tipo A, B o C.
    - Priorización de inventarios.

    NO la uses para:
    - Pronósticos.
    - EOQ.
    - Punto de reorden.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("classify_inventory_abc_tool")
    print("Problema:", problem)

    return f"Clasificación ABC realizada para: {problem}"


@tool
def calculate_eoq_tool(problem: str) -> str:
    """
    Calcula la Cantidad Económica de Pedido (EOQ).

    Úsala SOLO cuando el usuario pregunte por:
    - EOQ.
    - Cantidad económica de pedido.
    - Tamaño óptimo del lote.
    - Cantidad óptima de compra.

    NO la uses para:
    - Stock actual.
    - Clasificación ABC.
    - Pronóstico de demanda.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("calculate_eoq_tool")
    print("Problema:", problem)

    return f"EOQ calculado para: {problem}"