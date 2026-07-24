"""
base_solver.py

Clase base para todos los solvers de optimización.

Define el flujo común de ejecución:

    validate()
        ↓
    build_model()
        ↓
    optimize()
        ↓
    extract_solution()
        ↓
    build_response()
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseSolver(ABC):
    """
    Clase base para todos los modelos de optimización.
    """

    # ============================================================
    # PUBLIC API
    # ============================================================

    def solve(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Flujo estándar de todos los modelos de optimización.
        """

        self.validate(problem, context, analysis)

        mathematical_model = self.build_model(
            problem=problem,
            context=context,
            analysis=analysis,
        )

        self.optimize(mathematical_model)

        solution = self.extract_solution()

        return self.build_response(
            analysis=analysis,
            mathematical_model=mathematical_model,
            solution=solution,
        )

    # ============================================================
    # VALIDATION
    # ============================================================

    def validate(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
    ) -> None:
        """
        Validaciones generales.
        """

        if not problem:
            raise ValueError("Problem cannot be empty.")

        if analysis is None:
            raise ValueError("Analysis cannot be None.")

    # ============================================================
    # ABSTRACT METHODS
    # ============================================================

    @abstractmethod
    def build_model(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
    ) -> Any:
        """
        Construye el modelo matemático.
        """
        raise NotImplementedError

    @abstractmethod
    def optimize(
        self,
        mathematical_model: Any,
    ) -> None:
        """
        Ejecuta el modelo de optimización.
        """
        raise NotImplementedError

    @abstractmethod
    def extract_solution(
        self,
    ) -> dict[str, Any]:
        """
        Extrae la solución del solver.
        """
        raise NotImplementedError

    @abstractmethod
    def build_response(
        self,
        analysis: dict[str, Any],
        mathematical_model: Any,
        solution: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Construye la respuesta estructurada.
        """
        raise NotImplementedError