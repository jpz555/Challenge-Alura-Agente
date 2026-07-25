"""
agents/base/base_agent.py

Clase base para todos los agentes del sistema.
Define el contrato común que deberán implementar los agentes.
"""

from abc import ABC, abstractmethod

from agents.base.state import AgentState
from prompts.responses.responses import (INVENTORY_RESPONSE_PROMPT, ROUTING_RESPONSE_PROMPT, SCHEDULING_RESPONSE_PROMPT)


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
        de rutas. Este resumen será utilizado por el LLM
        únicamente para redactar una respuesta ejecutiva.
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
            # recommendation = ("La solución puede utilizarse operacionalmente.")

        elif status == "time_limit":
            status_text = (
                "El solver alcanzó el tiempo máximo configurado "
                "y encontró una solución factible."
            )
            # recommendation = (
            #     "Si se requiere una solución con menor GAP, "
            #     "puede incrementarse el tiempo máximo de optimización."
            #)
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
            # gap_text = "No disponible."
            gap_value = "No disponible"
            technical_conclusion = ("No fue posible calcular el GAP de optimalidad.")
            recommendation = ("Revise el resultado generado por el solver.")
            
        else:
            gap_value = f"{gap:.2%}"
             
            if status == "optimal":

                technical_conclusion = (
                    "La solución encontrada fue demostrada como óptima."
                )

                recommendation = (
                    "La solución puede utilizarse operacionalmente."
                )

            elif status == "time_limit":

                if gap <= 0.01:

                    technical_conclusion = (
                        "Se obtuvo una solución factible muy cercana al óptimo."
                    )

                    recommendation = (
                        "La solución puede utilizarse, aunque el solver "
                        "finalizó por límite de tiempo."
                    )

                elif gap <= 0.05:

                    technical_conclusion = (
                        "Se obtuvo una solución factible con una diferencia "
                        "moderada respecto a la mejor cota conocida."
                    )

                    recommendation = (
                        "Evaluar si el nivel de calidad obtenido satisface "
                        "los criterios operativos de la organización."
                    )

                else:

                    technical_conclusion = (
                        "El solver no logró demostrar la cercanía de la "
                        "solución encontrada al óptimo antes de finalizar."
                    )

                    recommendation = (
                        "Si se requiere reducir el GAP, puede incrementarse "
                        "el tiempo máximo de optimización para permitir que "
                        "el solver continúe la búsqueda."
                    )

            elif status == "infeasible":

                technical_conclusion = (
                    "El modelo no encontró una solución factible."
                )

                recommendation = (
                    "Revisar las restricciones, parámetros y datos de entrada."
                )

            else:

                technical_conclusion = (
                    "No fue posible generar una interpretación automática "
                    "del resultado."
                )

                recommendation = (
                    "Revisar el estado reportado por el solver."
                )

        # ==========================================================
        # Indicadores
        # ==========================================================

        objective_text = (
            f"{objective:,.2f}"
            if objective is not None
            else "No disponible"
        )

        runtime_text = (
            f"{runtime:.2f} segundos"
            if runtime is not None
            else "No disponible"
        )

        # ==========================================================
        # Resumen técnico
        # ==========================================================

        return f"""
                RESUMEN TÉCNICO

                MODELO MATEMÁTICO
                {model_name}

                ESTADO DEL SOLVER
                {status_text}

                INDICADORES

                - Modelo: {model_name}
                - Estado: {status}
                - Valor de la función objetivo: {objective_text}
                - Tiempo de ejecución: {runtime_text}
                - GAP de optimalidad: {gap_value}
                - Vehículos utilizados: {len(vehicles)}
                - Rutas generadas: {len(routes)}

                CONCLUSIÓN TÉCNICA

                {technical_conclusion}

                RECOMENDACIÓN TÉCNICA

                {recommendation}
                """
                          
    # Provisionales
    def _format_inventory_result(self, tool_result: dict) -> str:
        return str(tool_result)
    
    def _format_scheduling_result(self, tool_result: dict,) -> str:
        return str(tool_result)

    def _interpret_result(self, user_query: str, tool_name:str, tool_result: dict,context: str) -> str:
        formatted_result = self._format_tool_result(tool_name, tool_result)
        
        if tool_name  in ("optimize_routes", "estimate_delivery_time", "calculate_route_cost"):
            system_prompt = ROUTING_RESPONSE_PROMPT 
            
        elif tool_name in ("check_stock","forecast_demand", "reorder_point"):
            system_prompt = INVENTORY_RESPONSE_PROMPT

        elif tool_name in ("optimize_schedule", "assign_resource", "check_availability"):
            system_prompt = SCHEDULING_RESPONSE_PROMPT
        else:
            system_prompt = ROUTING_RESPONSE_PROMPT
        
        prompt = f"""
        {system_prompt}

        CONSULTA

        {user_query}

        CONTEXTO

        {context}

        RESUMEN TÉCNICO

        {formatted_result}
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
    
