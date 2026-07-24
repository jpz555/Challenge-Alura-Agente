"""
routing_solver.py

Dispatcher de modelos de optimización de Routing.

Responsabilidades
-----------------
- Seleccionar el solver adecuado.
- Delegar la resolución del problema.
- Mantener una interfaz única para todos los modelos.

No contiene lógica matemática.
No conoce Gurobi.
No conoce restricciones.
"""

from __future__ import annotations

from typing import Any

from tools.routing.solvers.hmdvrp_solver_grb import HMDVRPSolver
# from tools.routing.solvers.vrptw_solver import VRPTWSolver


class RoutingSolver:

    """
    Dispatcher de modelos de ruteo.
    """

    def __init__(self):

        self._solvers = {
            "HMDVRP": HMDVRPSolver(),
            # "VRPTW": VRPTWSolver(),

        }

    # ==============================================================
    # PUBLIC
    # ==============================================================

    def solve(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
        selected_model: dict[str, Any],
    ) -> dict[str, Any]:

        model_name = selected_model["selected_model"]

        solver = self._get_solver(model_name)

        return solver.solve(

            problem=problem,

            context=context,

            analysis=analysis,

        )

    def estimate_delivery_time(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
    ) -> dict[str, Any]:

        raise NotImplementedError(
            "estimate_delivery_time() not implemented."
        )

    def calculate_route_cost(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
    ) -> dict[str, Any]:

        raise NotImplementedError(
            "calculate_route_cost() not implemented."
        )

    # ==============================================================
    # PRIVATE
    # ==============================================================

    def _get_solver(
        self,
        model_name: str,
    ):

        solver = self._solvers.get(model_name)

        if solver is None:

            available = ", ".join(
                self._solvers.keys()
            )

            raise NotImplementedError(

                f"""
                Routing model '{model_name}' is not implemented.

                Available models:

                {available}
                """

            )

        return solver

    # ==============================================================
    # REGISTRATION
    # ==============================================================

    def register_solver(
        self,
        model_name: str,
        solver,
    ) -> None:

        self._solvers[model_name] = solver

    @property
    def available_models(self):

        return list(
            self._solvers.keys()
        )