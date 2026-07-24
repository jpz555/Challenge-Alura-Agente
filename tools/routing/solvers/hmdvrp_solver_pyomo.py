"""
hmdvrp_solver.py

Solver para el modelo Heterogeneous Multi-Depot Vehicle Routing Problem
(HMDVRP).

Implementación:
    - Pyomo
    - HiGHS
"""

from __future__ import annotations

from typing import Any

from pyomo.environ import (
    Binary,
    ConcreteModel,
    NonNegativeReals,
    Set,
    Param,
    Var,
    Constraint,
    Objective,
    SolverFactory,
    minimize,
    value,
)

from tools.base.base_solver import BaseSolver


class HMDVRPSolver(BaseSolver):
    """
    Solver para el modelo HMDVRP.
    """

    def __init__(self):

        self.model_name = "HMDVRP"

        self.model = None

        self.results = None

    # ============================================================
    # BUILD MODEL
    # ============================================================

    def build_model(
        self,
        problem: str,
        context: str,
        analysis: dict[str, Any],
    ) -> ConcreteModel:
        """
        Construye el modelo matemático.
        """

        routing_data = analysis["routing_data"]

        self.model = ConcreteModel(name=self.model_name)

        self._build_sets(routing_data)

        self._build_parameters(routing_data)

        self._build_variables()

        self._build_objective()

        self._build_constraints()

        return self.model

    # ============================================================
    # SETS
    # ============================================================

    def _build_sets(
        self,
        routing_data: dict[str, Any],
    ) -> None:
        """
        Construye los conjuntos.
        """

        depots = routing_data["depots"]

        customers = routing_data["customers"]

        vehicles = routing_data["vehicles"]

        self.model.D = Set(
            initialize=depots,
            ordered=True,
            doc="Depósitos",
        )

        self.model.C = Set(
            initialize=customers,
            ordered=True,
            doc="Clientes",
        )

        self.model.K = Set(
            initialize=vehicles,
            ordered=True,
            doc="Vehículos",
        )

        self.model.N = Set(
            initialize=depots + customers,
            ordered=True,
            doc="Todos los nodos",
        )

    # ============================================================
    # PARAMETERS
    # ============================================================

    def _build_parameters(
        self,
        routing_data: dict[str, Any],
    ) -> None:
        """
        Construye los parámetros.
        """

        distance_matrix = routing_data["distance_matrix"]

        demands = routing_data["demands"]

        vehicle_capacity = routing_data["vehicle_capacity"]

        vehicle_fixed_cost = routing_data.get(
            "vehicle_fixed_cost",
            {}
        )

        vehicle_variable_cost = routing_data.get(
            "vehicle_variable_cost",
            {}
        )

        #
        # Distancias
        #

        distance = {}

        for i in self.model.N:
            for j in self.model.N:

                distance[(i, j)] = distance_matrix[i][j]

        self.model.distance = Param(
            self.model.N,
            self.model.N,
            initialize=distance,
            mutable=False,
            default=0,
        )

        #
        # Demanda
        #

        self.model.demand = Param(
            self.model.C,
            initialize=demands,
            mutable=False,
            default=0,
        )

        #
        # Capacidad
        #

        self.model.capacity = Param(
            self.model.K,
            initialize=vehicle_capacity,
            mutable=False,
        )

        #
        # Costo fijo
        #

        self.model.fixed_cost = Param(
            self.model.K,
            initialize=vehicle_fixed_cost,
            mutable=False,
            default=0,
        )

        #
        # Costo variable
        #

        self.model.variable_cost = Param(
            self.model.K,
            initialize=vehicle_variable_cost,
            mutable=False,
            default=1,
        )

    # ============================================================
    # VARIABLES
    # ============================================================

    def _build_variables(self) -> None:
        """
        Construye las variables.
        """

        #
        # Arcos válidos
        #

        self.model.A = Set(
            dimen=2,
            initialize=[
                (i, j)
                for i in self.model.N
                for j in self.model.N
                if i != j
            ],
            ordered=True,
        )

        #
        # x[i,j,k]
        #

        self.model.x = Var(
            self.model.A,
            self.model.K,
            domain=Binary,
        )

        #
        # y[k]
        #

        self.model.y = Var(
            self.model.K,
            domain=Binary,
        )

        #
        # u[i]
        #

        self.model.u = Var(
            self.model.C,
            domain=NonNegativeReals,
            bounds=(0, len(self.model.C)),
        )
        
        # ============================================================
# OBJECTIVE
# ============================================================

def _build_objective(self) -> None:
    """
    Construye la función objetivo.
    """

    def objective_rule(model):

        transport_cost = sum(

            model.distance[i, j]

            * model.variable_cost[k]

            * model.x[i, j, k]

            for (i, j) in model.A

            for k in model.K

        )

        fixed_cost = sum(

            model.fixed_cost[k]

            * model.y[k]

            for k in model.K

        )

        return transport_cost + fixed_cost

    self.model.objective = Objective(

        rule=objective_rule,

        sense=minimize,

    )

# ============================================================
# CONSTRAINTS
# ============================================================

def _build_constraints(self) -> None:
    """
    Construye todas las restricciones.
    """

    self._customer_visit_constraint()

    self._flow_conservation_constraint()

    self._vehicle_capacity_constraint()

    self._depot_departure_constraint()

    self._depot_return_constraint()

    self._subtour_elimination_constraint()

# ============================================================
# CUSTOMER VISIT
# ============================================================

def _customer_visit_constraint(self) -> None:
    """
    Cada cliente debe ser visitado exactamente una vez.
    """

    def rule(model, customer):

        return (

            sum(

                model.x[i, j, k]

                for (i, j) in model.A

                for k in model.K

                if j == customer

            )

            ==

            1

        )

    self.model.customer_visit = Constraint(

        self.model.C,

        rule=rule,

    )

# ============================================================
# FLOW CONSERVATION
# ============================================================

def _flow_conservation_constraint(self) -> None:
    """
    Conservación de flujo.
    """

    def rule(model, vehicle, customer):

        incoming = sum(

            model.x[i, j, vehicle]

            for (i, j) in model.A

            if j == customer

        )

        outgoing = sum(

            model.x[i, j, vehicle]

            for (i, j) in model.A

            if i == customer

        )

        return incoming == outgoing

    self.model.flow_conservation = Constraint(

        self.model.K,

        self.model.C,

        rule=rule,

    )
    
    # ============================================================
# VEHICLE CAPACITY
# ============================================================

def _vehicle_capacity_constraint(self) -> None:
    """
    Restricción de capacidad de los vehículos.
    """

    def rule(model, vehicle):

        return (

            sum(

                model.demand[customer]

                *

                sum(

                    model.x[i, customer, vehicle]

                    for i in model.N

                    if (i, customer) in model.A

                )

                for customer in model.C

            )

            <=

            model.capacity[vehicle]

        )

    self.model.vehicle_capacity = Constraint(

        self.model.K,

        rule=rule,

    )


# ============================================================
# DEPOT DEPARTURE
# ============================================================

def _depot_departure_constraint(self) -> None:
    """
    Cada vehículo puede salir de un único depósito.
    """

    def rule(model, vehicle):

        return (

            sum(

                model.x[d, j, vehicle]

                for d in model.D

                for j in model.C

                if (d, j) in model.A

            )

            <=

            model.y[vehicle]

        )

    self.model.depot_departure = Constraint(

        self.model.K,

        rule=rule,

    )


# ============================================================
# DEPOT RETURN
# ============================================================

def _depot_return_constraint(self) -> None:
    """
    Todo vehículo utilizado debe regresar a un depósito.
    """

    def rule(model, vehicle):

        return (

            sum(

                model.x[i, d, vehicle]

                for d in model.D

                for i in model.C

                if (i, d) in model.A

            )

            <=

            model.y[vehicle]

        )

    self.model.depot_return = Constraint(

        self.model.K,

        rule=rule,

    )


# ============================================================
# SUBTOUR ELIMINATION (MTZ)
# ============================================================

def _subtour_elimination_constraint(self) -> None:
    """
    Eliminación de subtours mediante MTZ.
    """

    n = len(self.model.C)

    def rule(model, vehicle, i, j):

        #
        # No aplicar sobre el mismo nodo
        #

        if i == j:

            return Constraint.Skip

        #
        # Solo clientes
        #

        if (i, j) not in model.A:

            return Constraint.Skip

        return (

            model.u[i]

            -

            model.u[j]

            +

            n * model.x[i, j, vehicle]

            <=

            n - 1

        )

    self.model.subtour_elimination = Constraint(

        self.model.K,

        self.model.C,

        self.model.C,

        rule=rule,

    )