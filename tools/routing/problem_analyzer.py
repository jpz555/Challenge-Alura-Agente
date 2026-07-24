"""
problem_analyzer.py

Analiza el problema de optimización a partir de la consulta del usuario
y el contexto recuperado desde el RAG.

Responsabilidades
-----------------
- Identificar el objetivo del problema.
- Extraer las características del problema.
- Extraer los recursos disponibles.
- Extraer las reglas de negocio.

No selecciona el modelo matemático.
No construye el OptimizationModel.
"""

from __future__ import annotations

from typing import Any

class ProblemAnalyzer:
    def analyze(self,problem: str,context: str,) -> dict[str, Any]:

        text = f"{problem}\n\n{context}".lower()

        return {
            "problem": problem,
            "context": context,
            "objective": self._extract_objective(text),
            "features": self._extract_features(text),
            "resources": self._extract_resources(text),
            "business_rules": self._extract_business_rules(text),
            # "routing_data": self._extract_routing_data(context)
        }

    # ===============================================================
    # OBJECTIVE
    # ===============================================================

    def _extract_objective(self, text: str) -> dict:

        objective = {
            "type": "minimize_distance",
            "description": "Minimizar la distancia total recorrida."
        }

        rules = {
            "costo": (
                "minimize_cost",
                "Minimizar el costo total."
            ),
            "coste": (
                "minimize_cost",
                "Minimizar el costo total."
            ),
            "tiempo": (
                "minimize_time",
                "Minimizar el tiempo total."
            ),
            "emisiones": (
                "minimize_emissions",
                "Minimizar emisiones."
            ),
            "co2": (
                "minimize_emissions",
                "Minimizar emisiones."
            ),
            "nivel de servicio": (
                "maximize_service_level",
                "Maximizar el nivel de servicio."
            )
        }

        for keyword, value in rules.items():
            if keyword in text:
                objective["type"] = value[0]
                objective["description"] = value[1]
                break

        return objective

    # ===============================================================
    # FEATURES
    # ===============================================================

    def _extract_features(self, text: str) -> dict:

        # return {

        #     "multiple_depots": any(
        #         x in text
        #         for x in [
        #             "centro de distribución",
        #             "cd-",
        #             "multi depósito",
        #             "multiple depot"
        #         ]
        #     ),

        #     "heterogeneous_fleet": any(
        #         x in text
        #         for x in [
        #             "flota heterogénea",
        #             "t12",
        #             "r8",
        #             "tr30",
        #             "f5"
        #         ]
        #     ),

        #     "time_windows": any(
        #         x in text
        #         for x in [
        #             "ventana de tiempo",
        #             "horario",
        #             "08:00",
        #             "18:00"
        #         ]
        #     ),

        #     "priority_customers": any(
        #         x in text
        #         for x in [
        #             "hospital",
        #             "farmacia",
        #             "cliente prioritario"
        #         ]
        #     ),

        #     "cold_chain": any(
        #         x in text
        #         for x in [
        #             "cadena de frío",
        #             "refrigerado"
        #         ]
        #     ),

        #     "dynamic_requests": any(
        #         x in text
        #         for x in [
        #             "urgente",
        #             "nuevo pedido",
        #             "reoptimizar",
        #             "dinámico"
        #         ]
        #     ),

        #     "green_optimization": any(
        #         x in text
        #         for x in [
        #             "co2",
        #             "emisiones",
        #             "combustible",
        #             "verde"
        #         ]
        #     ),

        #     "split_deliveries": any(
        #         x in text
        #         for x in [
        #             "dividir entregas",
        #             "split delivery",
        #             "entrega parcial"
        #         ]
        #     )
        # }
        
        return {

        # ==========================================================
        # MULTI DEPOT
        # ==========================================================

        "multiple_depots": any(
            keyword in text
            for keyword in [

                "centro de distribución",
                "centros de distribución",
                "centro logistico",
                "centros logísticos",
                "cd-",
                "cd ",
                "bodega",
                "bodegas"

            ]
        ),

        # ==========================================================
        # HETEROGENEOUS FLEET
        # ==========================================================

        "heterogeneous_fleet": any(
            keyword in text
            for keyword in [

                "flota",

                "t12",
                "r8",
                "tr30",
                "f5",

                "camión",
                "camiones",

                "tractomula",
                "tractomulas",

                "vehículo",
                "vehículos",

                "vehículo refrigerado",
                "vehículos refrigerados",

                "furgón",
                "furgones"

            ]
        ),

        # ==========================================================
        # TIME WINDOWS
        # ==========================================================

        "time_windows": any(
            keyword in text
            for keyword in [

                "ventana de tiempo",
                "ventanas de tiempo",

                "horario",

                "08:00",
                "18:00",

                "hora de entrega"

            ]
        ),

        # ==========================================================
        # PRIORITY CUSTOMERS
        # ==========================================================

        "priority_customers": any(
            keyword in text
            for keyword in [

                "hospital",
                "hospitales",

                "farmacia",
                "farmacias",

                "cliente prioritario",
                "clientes prioritarios"

            ]
        ),

        # ==========================================================
        # COLD CHAIN
        # ==========================================================

        "cold_chain": any(
            keyword in text
            for keyword in [

                "cadena de frío",
                "refrigerado",
                "refrigerados",
                "temperatura controlada"

            ]
        ),

        # ==========================================================
        # DYNAMIC REQUESTS
        # ==========================================================

        "dynamic_requests": any(
            keyword in text
            for keyword in [

                "urgente",
                "nuevo pedido",
                "reoptimizar",
                "dinámico",
                "dinamico"

            ]
        ),

        # ==========================================================
        # GREEN
        # ==========================================================

        "green_optimization": any(
            keyword in text
            for keyword in [

                "co2",
                "emisiones",
                "carbono",
                "combustible",
                "verde",
                "sostenibilidad"

            ]
        ),

        # ==========================================================
        # SPLIT DELIVERY
        # ==========================================================

        "split_deliveries": any(
            keyword in text
            for keyword in [

                "split delivery",
                "dividir entregas",
                "entrega parcial",
                "entregas parciales"

            ]
        )

    }

    # ===============================================================
    # RESOURCES
    # ===============================================================

    def _extract_resources(self, text: str) -> dict:

        depots = []
        vehicles = []
        customer_types = []

        # ==========================================================
        # DEPOTS
        # ==========================================================

        if "centros de distribución" in text:
            depots.append("Corporate Distribution Centers")

        if "centro de distribución" in text:
            depots.append("Distribution Center")

        if "cd-01" in text:
            depots.append("CD-01")

        if "cd-02" in text:
            depots.append("CD-02")

        if "cd-03" in text:
            depots.append("CD-03")

        if "cd-04" in text:
            depots.append("CD-04")

        # ==========================================================
        # VEHICLES
        # ==========================================================

        vehicle_catalog = {

            "t12": "T12",

            "r8": "R8",

            "tr30": "TR30",

            "f5": "F5",

            "camión": "Truck",

            "camiones": "Truck",

            "tractomula": "Tractor",

            "tractomulas": "Tractor",

            "vehículo refrigerado": "Refrigerated Truck",

            "vehículos refrigerados": "Refrigerated Truck",

            "furgón": "Van",

            "furgones": "Van"

        }

        for keyword, vehicle in vehicle_catalog.items():

            if keyword in text:

                if vehicle not in vehicles:

                    vehicles.append(vehicle)

        # ==========================================================
        # CUSTOMER TYPES
        # ==========================================================

        customer_catalog = {

            "hospital": "Hospital",

            "hospitales": "Hospital",

            "farmacia": "Pharmacy",

            "farmacias": "Pharmacy",

            "retail": "Retail",

            "industria": "Industry"

        }

        for keyword, customer in customer_catalog.items():

            if keyword in text:

                if customer not in customer_types:

                    customer_types.append(customer)

        return {

            "depots": depots,

            "vehicles": vehicles,

            "customer_types": customer_types

    }
    # ===============================================================
    # BUSINESS RULES
    # ===============================================================

    def _extract_business_rules(self, text: str) -> dict:

        rules = {}

        if "48 horas" in text:
            rules["lead_time_hours"] = 48

        if "8 horas" in text:
            rules["max_driver_hours"] = 8

        if "99%" in text:
            rules["service_level"] = 0.99
        elif "97%" in text:
            rules["service_level"] = 0.97

        return rules
    
    # deprecated function 
    # def _extract_routing_data(self,context: str) -> dict:

    #     routing_data = {
    #         "depots": [],
    #         "fleet": [],
    #         "customers": [],
    #         "orders": [],
    #         "distance_matrix": []
    #     }

    #     current_sheet = None
    #     current_record = {}

    #     sheet_mapping = {
    #         "depots": "depots",
    #         "fleet": "fleet",
    #         "customers": "customers",
    #         "orders": "orders",
    #         "distancematrix": "distance_matrix"
    #     }

    #     for line in context.splitlines():

    #         line = line.strip()

    #         if not line:
    #             continue

    #         if line.startswith("# Hoja:"):

    #             if current_sheet and current_record:
    #                 routing_data[current_sheet].append(current_record)
    #                 current_record = {}

    #             sheet_name = line.replace("# Hoja:", "").strip().lower()
    #             current_sheet = sheet_mapping.get(sheet_name)

    #             continue

    #         if current_sheet is None:
    #             continue

    #         if ":" in line:

    #             key, value = line.split(":", 1)

    #             current_record[key.strip()] = value.strip()

    #     if current_sheet and current_record:
    #         routing_data[current_sheet].append(current_record)

    #     return routing_data