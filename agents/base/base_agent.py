"""
agents/base/base_agent.py

Clase base para todos los agentes del sistema.
Define el contrato común que deberán implementar los agentes.
"""

from abc import ABC, abstractmethod

from agents.base.state import AgentState


class BaseAgent(ABC):
    """
    Clase base para todos los agentes del sistema.
    """

    def __init__(self, name: str):
        self.name = name
    
    def _format_tool_result(self, tool_name: str, tool_result: dict) -> str:
        """
        Convierte el resultado de una herramienta en un
        resumen estructurado para el LLM.
        """
        if tool_name in  ("optimize_routes", "estimate_delivery_time","calculate_route_cost",):
            return self._format_routing_result(tool_result)
        
        elif tool_name in ("check_stock", "forecast_demand","reorder_point",):
            return self._format_inventory_result(tool_result)

        elif tool_name in ("optimize_schedule", "assign_resource","check_availability",):
            return self._format_scheduling_result(tool_result)

        return str(tool_result)
    
    def _format_routing_result(self,tool_result: dict) -> str:
        """
        Construye un resumen técnico del resultado de la optimización
        de rutas para que posteriormente el LLM únicamente lo redacte.
        """
        solution = tool_result.get("solution", {})
        selected_model = tool_result.get("selected_model", {})

        # Datos básicos
        # -------------------------
        model_name = selected_model.get("name", "No disponible")
        status = solution.get("status", "No disponible")
        objective = solution.get("objective_value")
        runtime = solution.get("execution_time")
        gap = solution.get("gap")
        vehicles = solution.get("vehicles_used", [])
        routes = solution.get("routes", [])
        # -------------------------
        # Interpretación del estado
        # -------------------------
        if status == "optimal":
            status_text = ("El solver encontró una solución óptima.")
            recommendation = ("La solución puede utilizarse operacionalmente.")

        elif status == "time_limit":
            status_text = (
                "El solver alcanzó el tiempo máximo configurado "
                "y encontró una solución factible."
            )
            recommendation = (
                "Si se requiere una solución con menor GAP, "
                "puede incrementarse el tiempo máximo de optimización."
            )
        elif status == "infeasible":
            status_text = (
                "No fue posible encontrar una solución factible."
            )
            recommendation = (
                "Revise las restricciones y los datos del problema."
            )
        else:
            status_text = (
                f"El solver finalizó con estado '{status}'."
            )
            recommendation = (
                "Revise el resultado del proceso de optimización."
            )

        # -------------------------
        # Interpretación del GAP
        # -------------------------

        if gap is None:
            gap_text = "No disponible."
            gap_value = "No disponible"

        else:
            gap_value = f"{gap:.2%}"
            if gap <= 0.01:
                gap_text = (
                    "El solver demostró una solución muy cercana al óptimo."
                )
            elif gap <= 0.05:
                gap_text = (
                    "Existe una pequeña diferencia entre la mejor solución encontrada "
                    "y la mejor cota conocida."
                )
            else:
                gap_text = (
                    "El solver no alcanzó a demostrar qué tan cercana es la "
                    "solución encontrada al óptimo antes de finalizar."
                )

        # -------------------------
        # Costo
        # -------------------------

        if objective is None:

            objective_text = "No disponible"

        else:

            objective_text = f"{objective:,.2f}"

        # -------------------------
        # Tiempo
        # -------------------------

        if runtime is None:

            runtime_text = "No disponible"

        else:

            runtime_text = f"{runtime:.2f} segundos"

        # -------------------------
        # Resumen técnico
        # -------------------------

        return f"""
                MODELO SELECCIONADO
                {model_name}

                ESTADO DEL SOLVER
                {status_text}

                INDICADORES

                - Costo objetivo: {objective_text}
                - Tiempo de ejecución: {runtime_text}
                - GAP: {gap_value}
                - Vehículos utilizados: {len(vehicles)}
                - Rutas generadas: {len(routes)}

                INTERPRETACIÓN TÉCNICA

                {gap_text}

                RECOMENDACIÓN TÉCNICA

                {recommendation}
                """
                
    # Provisionales
    def _format_inventory_result(self, tool_result: dict) -> str:
        return str(tool_result)
    
    def _format_scheduling_result(self, tool_result: dict,) -> str:
        return str(tool_result)

    def _interpret_result(self, user_query: str, tool_name:str, tool_result: dict,context: str) -> str:
        """
        Interpreta el resultado devuelto por una herramienta utilizando el LLM.
        """
        formatted_result = self._format_tool_result(tool_name,tool_result)
        
        prompt = f"""
        Eres un consultor senior en Logística, Investigación de Operaciones y Cadena de Suministro.

        Tu función consiste únicamente en interpretar el resultado producido por una herramienta del sistema.

        CONSULTA DEL USUARIO
        --------------------
        {user_query}

        CONTEXTO CORPORATIVO
        --------------------
        {context}

        RESULTADO DE LA HERRAMIENTA
        ---------------------------
        {formatted_result}

        INSTRUCCIONES

        1. Analiza únicamente la información entregada.
        2. No inventes datos.
        3. No inventes restricciones.
        4. No inventes algoritmos.
        5. No propongas cambiar el algoritmo matemático.
        6. No sugieras técnicas de optimización diferentes.
        7. No afirmes que el modelo matemático está mal construido.
        8. Si el estado es "time_limit", explica únicamente que el solver alcanzó el tiempo máximo configurado y encontró una solución factible.
        9. Si existe un GAP, explica qué significa para el usuario de negocio sin entrar en detalles matemáticos complejos.
        10. Basa todas las conclusiones únicamente en la información recibida.

        Debes responder utilizando exclusivamente la estructura indicada a continuación.
        - No cambies los títulos.
        - No omitas ninguna sección.
        - Si algún indicador no está disponible, escribe "No disponible".
        - No agregues nuevas secciones.

        ## Resumen Ejecutivo
        ...
        ## Estado de la Solución
        ...
        ## Indicadores
        - Estado:
        - Modelo:
        - Tiempo de ejecución:
        - GAP:
        - Resultado principal:
        ## Interpretación
        ...
        ## Recomendación
        ...

        No agregues secciones adicionales.
        """
        response = self.llm.invoke(prompt)
        return response.content
    
    @abstractmethod
    def invoke(self, state: AgentState) -> AgentState:
        """
        Ejecuta la lógica del agente.

        Parameters
        ----------
        state : AgentState
            Estado compartido del flujo.

        Returns
        -------
        AgentState
            Estado actualizado.
        """
        raise NotImplementedError
    
