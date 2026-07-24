"""
Funciones Tool para Scheduling.
"""

from langchain_core.tools import tool


@tool
def optimize_schedule_tool(problem: str) -> str:
    """
    Optimiza la programación de actividades y recursos.

    Úsala SOLO cuando el usuario solicite:
    - Optimizar una programación.
    - Generar un cronograma óptimo.
    - Minimizar tiempos de operación.
    - Resolver un problema de scheduling.

    NO la uses para:
    - Asignar un recurso específico.
    - Consultar disponibilidad.
    - Programar mantenimientos.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("optimize_schedule_tool")
    print("Problema:", problem)

    return f"Programación optimizada para: {problem}"


@tool
def assign_resource_tool(problem: str) -> str:
    """
    Asigna recursos a una actividad o tarea.

    Úsala SOLO cuando el usuario pregunte por:
    - Asignación de recursos.
    - Asignación de operarios.
    - Asignación de vehículos.
    - Distribución de recursos.

    NO la uses para:
    - Optimizar cronogramas completos.
    - Consultar disponibilidad.
    - Balancear carga de trabajo.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("assign_resource_tool")
    print("Problema:", problem)

    return f"Recursos asignados para: {problem}"


@tool
def check_availability_tool(problem: str) -> str:
    """
    Consulta la disponibilidad de un recurso.

    Úsala SOLO cuando el usuario pregunte por:
    - Disponibilidad de vehículos.
    - Disponibilidad de operarios.
    - Disponibilidad de equipos.
    - Disponibilidad de recursos.

    NO la uses para:
    - Asignar recursos.
    - Optimizar cronogramas.
    - Balancear carga.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("check_availability_tool")
    print("Problema:", problem)

    return f"Disponibilidad consultada para: {problem}"


@tool
def balance_workload_tool(problem: str) -> str:
    """
    Balancea la carga de trabajo entre recursos.

    Úsala SOLO cuando el usuario pregunte por:
    - Balanceo de carga.
    - Distribución equitativa del trabajo.
    - Sobrecarga de recursos.
    - Nivelación de carga.

    NO la uses para:
    - Consultar disponibilidad.
    - Programar mantenimientos.
    - Asignar un único recurso.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("balance_workload_tool")
    print("Problema:", problem)

    return f"Carga de trabajo balanceada para: {problem}"


@tool
def assign_shift_tool(problem: str) -> str:
    """
    Asigna turnos de trabajo al personal.

    Úsala SOLO cuando el usuario pregunte por:
    - Asignación de turnos.
    - Programación de turnos.
    - Horarios del personal.
    - Distribución de jornadas laborales.

    NO la uses para:
    - Programación de mantenimiento.
    - Balanceo de carga.
    - Optimización general del cronograma.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("assign_shift_tool")
    print("Problema:", problem)

    return f"Turnos asignados para: {problem}"


@tool
def schedule_maintenance_tool(problem: str) -> str:
    """
    Programa actividades de mantenimiento preventivo o correctivo.

    Úsala SOLO cuando el usuario pregunte por:
    - Programación de mantenimiento.
    - Agenda de mantenimiento.
    - Mantenimiento preventivo.
    - Mantenimiento correctivo.

    NO la uses para:
    - Asignación de turnos.
    - Balanceo de carga.
    - Optimización de rutas.
    """

    print("\n========== TOOL EJECUTADA ==========")
    print("schedule_maintenance_tool")
    print("Problema:", problem)

    return f"Mantenimiento programado para: {problem}"