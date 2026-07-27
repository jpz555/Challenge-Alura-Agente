"""
hmdvrp_solver.py

Solver para el modelo Heterogeneous Multi-Depot Vehicle Routing Problem
(HMDVRP).

Responsabilidades
-----------------
1. Construir el modelo matemático.
2. Resolver el modelo mediante Gurobi.
3. Extraer la solución.
4. Devolver una respuesta estructurada.

No consulta el RAG.
No interpreta lenguaje natural.
"""

from __future__ import annotations
from typing import Any
import gurobipy as gp
from gurobipy import GRB

from tools.base.base_solver import BaseSolver

class HMDVRPSolver(BaseSolver):
    """
    Solver para HMDVRP.
    """
    def __init__(self):

        self.model_name = "HMDVRP"

    # ============================================================
    # BUILD MODEL
    # ============================================================
    def build_model(self,problem: str,context: str,analysis: dict[str, Any]) -> gp.Model:
        """
        Construye el modelo matemático.
        """
        routing_data = analysis["routing_data"]
        self._build_sets(routing_data)
        self._build_parameters(routing_data)
        self.model = gp.Model(self.model_name)
        self._build_variables()
        self._build_objective()
        self._build_constraints()
        return self.model

    # SETS
    def _build_sets(self,routing_data: dict[str, Any]) -> None:
        """
        Construye los conjuntos del modelo.
        """
        self.depots = routing_data["depots"]
        self.customers = routing_data["customers"]
        self.nodes = self.depots + self.customers
        self.vehicles = routing_data["vehicles"]
        
    # PARAMETERS
    def _build_parameters(self,routing_data: dict[str, Any]) -> None:
        """
        Construye todos los parámetros del modelo.
        """
        self.distance_matrix = routing_data["distance_matrix"]
        self.travel_time = routing_data.get(
            "travel_time",
            self.distance_matrix
        )
        self.demands = routing_data["demands"]
        self.vehicle_capacity = routing_data["vehicle_capacity"]
        self.vehicle_fixed_cost = routing_data.get(
            "vehicle_fixed_cost",
            {}
        )
        print(self.vehicle_fixed_cost)
        
        self.vehicle_variable_cost = routing_data.get(
            "vehicle_variable_cost",
            {}
        )
        print(self.vehicle_variable_cost)
        self.max_route_time = routing_data.get(
            "max_route_time",
            None
        )

        self.business_rules = routing_data.get(
            "business_rules",
            {}
        )

    # ============================================================
    # VARIABLES
    # ============================================================
    def _build_variables(self) -> None:
        """
        Variables de decisión.
        """
        #
        # x[i,j,k]
        # El vehículo k viaja de i hacia j
        #
        self.valid_arcs = [
            (i, j, k)
            for k in self.vehicles
            for i in self.nodes
            for j in self.nodes
            if i != j
        ]

        self.x = self.model.addVars(
            self.valid_arcs,
            vtype=GRB.BINARY,
            name="x"
        )

        #
        # y[k]
        # Vehículo utilizado
        #
        self.y = self.model.addVars(
            self.vehicles,
            vtype=GRB.BINARY,
            name="y"
        )
        
        # u[i]
        # Variables MTZ para eliminar subtours
        #
        self.u = self.model.addVars(
            self.customers,
            lb=1,
            ub=len(self.customers),
            vtype=GRB.CONTINUOUS,
            name="u"
        )
        

    # ============================================================
    # OBJECTIVE
    # ============================================================
    def _build_objective(self) -> None:
        """
        Minimizar costo total.
        """
        transport_cost = gp.quicksum(
            self.distance_matrix[i][j]
            * self.vehicle_variable_cost.get(k, 1)
            * self.x[i, j, k]
            for (i, j, k) in self.valid_arcs
        )
        
        fixed_cost = gp.quicksum(
            self.vehicle_fixed_cost.get(k, 0)
            * self.y[k]
            for k in self.vehicles
        )

        self.model.setObjective(
            transport_cost + fixed_cost,
            GRB.MINIMIZE
        )
            
    # ============================================================
    # CONSTRAINTS
    # ============================================================
    
    def _build_constraints(self) -> None:
        """
        Construye todas las restricciones del modelo.
        """
        self._customer_visit_constraint()
        self._flow_conservation_constraint()
        self._vehicle_capacity_constraint()
        self._depot_departure_constraint()
        self._depot_return_constraint()
        self._vehicle_activation_constraint()
        self._maximum_route_time_constraint()
        self._subtour_elimination_constraint()


    # ============================================================
    # CUSTOMER VISIT
    # ============================================================

    def _customer_visit_constraint(self) -> None:
        """
        Cada cliente debe ser visitado exactamente una vez.
        """

        for customer in self.customers:

            self.model.addConstr(

                gp.quicksum(
                    self.x[i, j, k]
                    for (i, j, k) in self.valid_arcs
                    if j == customer
                )
                == 1,

                name=f"visit_{customer}"

            )


    # ============================================================
    # FLOW CONSERVATION
    # ============================================================

    def _flow_conservation_constraint(self) -> None:
        """
        Conservación de flujo.
        Todo vehículo que entra a un nodo debe salir.
        """

        for vehicle in self.vehicles:

            for customer in self.customers:

                incoming = gp.quicksum(

                    self.x[i, j, vehicle]

                    for (i, j, k) in self.valid_arcs

                    if k == vehicle and j == customer

                )

                outgoing = gp.quicksum(

                    self.x[i, j, vehicle]

                    for (i, j, k) in self.valid_arcs

                    if k == vehicle and i == customer

                )

                self.model.addConstr(

                    incoming == outgoing,

                    name=f"flow_{vehicle}_{customer}"

                )


    # ============================================================
    # VEHICLE CAPACITY
    # ============================================================

    def _vehicle_capacity_constraint(self) -> None:
        """
        Restricción de capacidad.
        """

        for vehicle in self.vehicles:

            self.model.addConstr(

                gp.quicksum(

                    self.demands[customer]

                    *

                    gp.quicksum(

                        self.x[i, j, vehicle]

                        for (i, j, k) in self.valid_arcs

                        if k == vehicle and j == customer

                    )

                    for customer in self.customers

                )

                <=

                self.vehicle_capacity[vehicle],

                name=f"capacity_{vehicle}"

            )


    # ============================================================
    # DEPOT DEPARTURE
    # ============================================================

    def _depot_departure_constraint(self) -> None:
        """
        Cada vehículo sale de un único depósito.
        """

        for vehicle in self.vehicles:

            self.model.addConstr(

                gp.quicksum(

                    self.x[i, j, vehicle]

                    for (i, j, k) in self.valid_arcs

                    if (
                        k == vehicle
                        and i in self.depots
                        and j in self.customers
                    )

                )

                ==

                self.y[vehicle],

                name=f"departure_{vehicle}"

            )


    # ============================================================
    # DEPOT RETURN
    # ============================================================

    def _depot_return_constraint(self) -> None:
        """
        Todo vehículo debe regresar a un depósito.
        """

        for vehicle in self.vehicles:

            self.model.addConstr(

                gp.quicksum(

                    self.x[i, j, vehicle]

                    for (i, j, k) in self.valid_arcs

                    if (
                        k == vehicle
                        and i in self.customers
                        and j in self.depots
                    )

                )

                ==

                self.y[vehicle],

                name=f"return_{vehicle}"

            )


    # ============================================================
    # VEHICLE ACTIVATION
    # ============================================================

    def _vehicle_activation_constraint(self) -> None:
        """
        Activación del vehículo.
        """

        for (i, j, k) in self.valid_arcs:

            self.model.addConstr(

                self.x[i, j, k]

                <=

                self.y[k],

                name=f"activation_{i}_{j}_{k}"

            )
            
    def _maximum_route_time_constraint(self) -> None:
        """
        Ningún vehículo puede superar el tiempo máximo permitido.
        """

        if self.max_route_time is None:
            return

        for vehicle in self.vehicles:

            self.model.addConstr(

                gp.quicksum(
                    self.travel_time[i][j]
                    * self.x[i, j, vehicle]

                    for (i, j, k) in self.valid_arcs

                    if k == vehicle

                )

                <=

                self.max_route_time,

                name=f"route_time_{vehicle}"

            )


    # ============================================================
    # SUBTOUR ELIMINATION (MTZ)
    # ============================================================

    def _subtour_elimination_constraint(self) -> None:
        """
        Eliminación de subtours mediante restricciones MTZ.
        """

        n = len(self.customers)

        for (i, j, vehicle) in self.valid_arcs:

            if i not in self.customers:
                continue

            if j not in self.customers:
                continue

            self.model.addConstr(

                self.u[i]
                -
                self.u[j]
                +
                n * self.x[i, j, vehicle]
                <=
                n - 1,

                name=f"mtz_{vehicle}_{i}_{j}"

            )
                    
    # ============================================================
    # OPTIMIZATION
    # ============================================================

    def optimize(
        self,
        mathematical_model: gp.Model,
    ) -> None:
        """
        Ejecuta el modelo de optimización.
        """
        # Esta configuración es para reducir el tiempo de computo
        # Tiempo máximo (3 minutos)
        mathematical_model.setParam("TimeLimit", 180)

        # Gap máximo permitido (1%)
        mathematical_model.setParam("MIPGap", 0.01)

        # Utilizar todos los núcleos disponibles
        mathematical_model.setParam("Threads", 0)


        mathematical_model.optimize()

    # ============================================================
    # EXTRACT SOLUTION
    # ============================================================

    def extract_solution(self,) -> dict[str, Any]:
        """
        Extrae la solución del modelo optimizado.
        """
        
        status = self.model.Status

        # No existe ninguna solución
    
        if self.model.SolCount == 0:
            return {
                "status": "infeasible",
                "objective_value": None,
                "routes": [],
                "vehicles_used": [],
                "execution_time": self.model.Runtime,
                "gap": None,
            }

        # Existe al menos una solución
        routes = self._extract_routes()
        vehicles = self._extract_used_vehicles()

        if status == GRB.OPTIMAL:
            solution_status = "optimal"
        elif status == GRB.TIME_LIMIT:
            solution_status = "time_limit"
        elif status == GRB.SUBOPTIMAL:
            solution_status = "suboptimal"
        else:
            solution_status = "feasible"
        return {
            "status": solution_status,
            "objective_value": self.model.ObjVal,
            "routes": routes,
            "vehicles_used": vehicles,
            "execution_time": self.model.Runtime,
            "gap": self.model.MIPGap,
        }

    # ============================================================
    # ROUTE EXTRACTION
    # ============================================================

    def _extract_routes(self) -> list[dict[str, Any]]:
        """
        Extrae las rutas generadas para cada vehículo.
        """
        routes = []
        for vehicle in self.vehicles:
            vehicle_route = []
            for (i, j, k) in self.valid_arcs:
                if k != vehicle:
                    continue
                if self.x[i, j, k].X > 0.5:
                    vehicle_route.append({
                        "from": i,
                        "to": j,
                        "vehicle": vehicle
                    })

            if vehicle_route:
                routes.append({
                    "vehicle": vehicle,
                    "route": vehicle_route
                })

        return routes
            


    # ============================================================
    # USED VEHICLES
    # ============================================================

    def _extract_used_vehicles(self) -> list[Any]:
        """
        Obtiene los vehículos utilizados.
        """

        used = []

        for vehicle in self.vehicles:

            if self.y[vehicle].X > 0.5:

                used.append(vehicle)

        return used

    # ============================================================
    # RESPONSE
    # ============================================================

    def build_response(self, analysis: dict[str, Any],mathematical_model: gp.Model, solution: dict[str, Any]) -> dict[str, Any]:
        """
        Construye la respuesta estructurada del solver.
        """

        return {
            "status": solution["status"],
            "model": self.model_name,
            "analysis": analysis,
            "mathematical_model": {
                "objective": "Minimize total transportation cost",
                "variables": [

                    "x[i,j,k]",

                    "y[k]",

                    "u[i]"

                ],

                "constraints": [
                    "Customer visit",
                    "Flow conservation",
                    "Vehicle capacity",
                    "Depot departure",
                    "Depot return",
                    "Subtour elimination",
                    "Maximum route time"

                ]

            },

            "solution": solution

        }