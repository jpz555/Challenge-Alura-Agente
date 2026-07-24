"""
routing_engine.py

Orquestador del dominio Routing.

Responsabilidades
-----------------
1. Analizar el problema.
2. Seleccionar el modelo matemático.
3. Resolver el problema.
4. Formatear la respuesta.

No contiene lógica de optimización.
No conoce Gurobi.
No conoce modelos matemáticos.
"""

from __future__ import annotations
from pathlib import Path

from tools.data.corporate_data_loader import CorporateDataLoader
from tools.routing.problem_analyzer import ProblemAnalyzer
from tools.routing.rule_engine import RuleEngine
from tools.routing.routing_solver import RoutingSolver
from tools.routing.response_formatter import ResponseFormatter


class RoutingEngine:

    def __init__(self):

        self.problem_analyzer = ProblemAnalyzer()

        self.rule_engine = RuleEngine()

        self.routing_solver = RoutingSolver()

        self.response_formatter = ResponseFormatter()

    ####################################################################
    # PUBLIC API
    ####################################################################

    def optimize_routes(self,problem: str,context: str) -> dict:

        analysis = self.problem_analyzer.analyze(problem, context)

        # print("\n========== ANALYSIS ==========")
        # print(analysis)
        
        selected_model = self.rule_engine.select_model(analysis)
        
        print(selected_model)
        
        loader = CorporateDataLoader(Path("documents/data/corporate_data.xlsx"))
        
        routing_data = loader.load()


        analysis["routing_data"] = routing_data

        solution = self.routing_solver.solve(problem=problem,
                                             context=context,
                                             analysis=analysis,
                                             selected_model=selected_model
            )

        return self.response_formatter.format_solution(
            problem=problem,
            analysis=analysis,
            selected_model=selected_model,
            solution=solution,
        )

    ####################################################################
    # DELIVERY TIME
    ####################################################################

    def estimate_delivery_time(self,problem: str,context: str,) -> dict:

        analysis = self.problem_analyzer.analyze(
            problem,
            context,
        )

        return self.routing_solver.estimate_delivery_time(
            problem=problem,
            context=context,
            analysis=analysis,

        )

    ####################################################################
    # ROUTE COST
    ####################################################################

    def calculate_route_cost(self,problem: str,context: str) -> dict:
        analysis = self.problem_analyzer.analyze(
            problem,
            context,
        )

        return self.routing_solver.calculate_route_cost(
            problem=problem,
            context=context,
            analysis=analysis,

        )