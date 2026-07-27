"""
rule_engine.py

Motor de inferencia para seleccionar el modelo matemático
más apropiado para resolver un problema de ruteo.

Responsabilidades
-----------------
- Evaluar el análisis del problema.
- Seleccionar el modelo matemático.
- Justificar la decisión.

No conoce Gurobi.
No construye OptimizationModel.
No resuelve problemas.
"""

from __future__ import annotations

from typing import Any


class RuleEngine:

    MODEL_RULES = {

        "HMDVRP": {

            "multiple_depots": 3,
            "heterogeneous_fleet": 3,
            "objective:minimize_distance": 2,
            "!dynamic_requests": 1,
            "!time_windows": 1

        },

        "VRPTW": {

            "time_windows": 5,
            "objective:minimize_time": 3,
            "priority_customers": 2

        },

        "DVRP": {

            "dynamic_requests": 10

        },

        "GVRP": {

            "green_optimization": 7,
            "objective:minimize_emissions": 3

        },

        "SDVRP": {

            "split_deliveries": 10

        },

        "CVRP": {

            "!multiple_depots": 5,
            "!heterogeneous_fleet": 5

        }

    }

    FEATURE_MESSAGES = {

        "multiple_depots":
            "Se detectaron múltiples centros de distribución.",

        "heterogeneous_fleet":
            "Se detectó una flota heterogénea.",

        "time_windows":
            "Existen ventanas de tiempo.",

        "dynamic_requests":
            "Se detectaron pedidos dinámicos.",

        "green_optimization":
            "El problema tiene objetivos ambientales.",

        "split_deliveries":
            "Se permiten entregas divididas.",

        "priority_customers":
            "Existen clientes prioritarios."

    }

    OBJECTIVE_MESSAGES = {

        "minimize_distance":
            "El objetivo es minimizar la distancia.",

        "minimize_cost":
            "El objetivo es minimizar el costo.",

        "minimize_time":
            "El objetivo es minimizar el tiempo.",

        "minimize_emissions":
            "El objetivo es minimizar emisiones.",

        "maximize_service_level":
            "El objetivo es maximizar el nivel de servicio."

    }

    def select_model(
        self,
        analysis: dict[str, Any],
    ) -> dict[str, Any]:

        evaluations = []

        for model_name, rules in self.MODEL_RULES.items():

            evaluations.append(

                self._evaluate_model(
                    model_name=model_name,
                    rules=rules,
                    analysis=analysis,
                )

            )

        best = max(
            evaluations,
            key=lambda x: x["score"]
        )

        best["confidence"] = round(
            best["score"] / best["max_score"],
            2
        )

        return best

    ##################################################################
    # PRIVATE
    ##################################################################

    def _evaluate_model(
        self,
        model_name: str,
        rules: dict,
        analysis: dict,
    ) -> dict:

        score = 0

        reasoning = []

        triggered = []

        not_triggered = []

        features = analysis["features"]

        objective = analysis["objective"]["type"]

        max_score = sum(rules.values())

        for rule, weight in rules.items():

            if rule.startswith("objective:"):

                expected = rule.split(":")[1]

                if objective == expected:

                    score += weight

                    reasoning.append(
                        self.OBJECTIVE_MESSAGES.get(
                            expected,
                            expected
                        )
                    )

                    triggered.append(rule)

                else:

                    not_triggered.append(rule)

                continue

            negative = rule.startswith("!")

            feature = rule.replace("!", "")

            value = features.get(feature, False)

            satisfied = not value if negative else value

            if satisfied:

                score += weight

                if not negative:

                    reasoning.append(

                        self.FEATURE_MESSAGES.get(
                            feature,
                            feature
                        )

                    )

                triggered.append(rule)

            else:

                not_triggered.append(rule)

        return {

            "selected_model": model_name,

            "score": score,

            "max_score": max_score,

            "reasoning": reasoning,

            "rules_triggered": triggered,

            "rules_not_triggered": not_triggered

        }
        
    # estimate delivery time
    def extract_route(self,problem: str, context: str):
        """
        Extrae la ruta desde el contexto.
        """
        # TODO:
        # Aquí reutilizaremos el mismo mecanismo que ya usa
        # optimize_routes() para obtener los datos.

        return {
            "origin": "Barranquilla",
            "destination": "Cartagena",
            "travel_time": 3.8
        } 