"""
response_formatter.py

Formateador de respuestas para el dominio Routing.

Responsabilidades
-----------------
- Construir una respuesta uniforme para cualquier modelo de ruteo.
- Separar la lógica de presentación de la lógica de optimización.
- No conoce Gurobi.
- No conoce modelos matemáticos.
"""

from __future__ import annotations

from typing import Any


class ResponseFormatter:

    """
    Formatea la respuesta devuelta por cualquier RoutingSolver.
    """

    ####################################################################
    # PUBLIC API
    ####################################################################

    def format_solution(
        self,
        problem: str,
        analysis: dict[str, Any],
        selected_model: dict[str, Any],
        solution: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Construye la respuesta estructurada final.
        """

        return {

            "status": solution.get("status", "unknown"),

            "problem": problem,

            "selected_model": {

                "name": selected_model.get("selected_model"),

                "confidence": selected_model.get("confidence"),

                "score": selected_model.get("score"),

                "reasoning": selected_model.get(
                    "reasoning",
                    []
                )

            },

            "analysis": {

                "objective": analysis.get("objective"),

                "features": analysis.get("features"),

                "resources": analysis.get("resources"),

                "business_rules": analysis.get(
                    "business_rules"
                )

            },

            "optimization": solution.get(
                "mathematical_model",
                {}
            ),

            "solution": solution.get(
                "solution",
                {}
            )

        }

    ####################################################################
    # OPTIONAL
    ####################################################################

    def format_error(
        self,
        message: str,
    ) -> dict[str, Any]:

        return {

            "status": "error",

            "message": message

        }