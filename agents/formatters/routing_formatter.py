from agents.formatters.base_formatter import BaseFormatter

class RoutingFormatter(BaseFormatter):

    # def format(self, tool_name: str, tool_result: dict) -> dict:

    #     if tool_name == "optimize_routes":
    #         return self._format_optimization(tool_result)

    #     elif tool_name in (
    #         "estimate_delivery_time",
    #         "calculate_route_cost",
    #     ):
    #         return self._format_calculation(tool_result)

    #     return {
    #         "summary": "Resultado no soportado.",
    #         "status": "",
    #         "indicators": {},
    #         "technical_conclusion": "",
    #         "recommendation": "",
    #     }
    
    def format(self,tool_name: str,tool_result: dict) -> str:

        if tool_name == "optimize_routes":
            return self._format_routing_result(tool_result)

        elif tool_name in ("estimate_delivery_time","calculate_route_cost"):
            return str(tool_result)
        
        return str(tool_result)
    
    def _format_routing_result(self, tool_result: dict) -> str:
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
    def format_delivery_time(self,result: dict) -> dict:

        if result["status"] == "error":
            return {
                "response": result["message"]
            }

        response = f"""
                ## Resumen Ejecutivo
                Se estimó el tiempo de entrega solicitado.

                ## Resultado

                - Ruta: {result["origin"]} → {result["destination"]}
                - Tiempo estimado: {result["estimated_time"]:.2f} {result["unit"]}

                ## Interpretación

                La estimación corresponde al tiempo esperado de desplazamiento para la ruta consultada.

                ## Recomendación

                Utilice esta información para planificar la operación logística y coordinar la entrega.
        """
        return {
            "status": "success",
            "response": response.strip(),
            "technical_summary": result
        }