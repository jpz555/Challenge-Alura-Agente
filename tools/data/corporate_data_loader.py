"""
=========================================================
Corporate Data Loader
=========================================================

Responsabilidad:
    Leer el archivo CorporateData.xlsx y devolver todas las
    hojas como estructuras de datos.

Este componente NO contiene lógica de negocio.
Únicamente carga los datos estructurados.

=========================================================
"""

from pathlib import Path

import pandas as pd


class CorporateDataLoader:

    def __init__(self, data_file: Path):
        self.data_file = Path(data_file)

    # =====================================================
    # CARGAR TODO EL EXCEL
    # =====================================================
    def load(self) -> dict:
        workbook = pd.read_excel(self.data_file, sheet_name=None)

        # data = {}
        # dataframe = dataframe.fillna("")
        # data[sheet_name] = dataframe.to_dict(orient="records")

        depots_df = workbook["Depots"].fillna("")
        customers_df = workbook["Customers"].fillna("")
        fleet_df = workbook["Fleet"].fillna("")
        orders_df = workbook["Orders"].fillna("")
        distance_df = workbook["DistanceMatrix"].fillna("")
        depots = depots_df["depot_id"].tolist()
        customers = customers_df["customer_id"].tolist()
        vehicles = fleet_df["vehicle_id"].tolist()
        demands = (
            orders_df
            .groupby("customer_id")["quantity"]
            .sum()
            .to_dict()
        )

        vehicle_capacity = dict(
            zip(
                fleet_df["vehicle_id"],
                fleet_df["capacity_kg"]
            )
        )

        vehicle_fixed_cost = dict(
            zip(
                fleet_df["vehicle_id"],
                fleet_df["fixed_cost"]
            )
        )

        vehicle_variable_cost = dict(
            zip(
                fleet_df["vehicle_id"],
                fleet_df["variable_cost"]
            )
        )

        distance_matrix = {}

        for _, row in distance_df.iterrows():
            origin = row["origin"]
            destination = row["destination"]
            distance = row["distance_km"]
            if origin not in distance_matrix:
                distance_matrix[origin] = {}
            distance_matrix[origin][destination] = distance
                      
        return {
            "depots": depots,
            "customers": customers,
            "vehicles": vehicles,
            "demands": demands,
            "distance_matrix": distance_matrix,
            "vehicle_capacity": vehicle_capacity,
            "vehicle_fixed_cost": vehicle_fixed_cost,
            "vehicle_variable_cost": vehicle_variable_cost,
        }
        
    # RESUMEN PARA ANALYTICS
    # =====================================================
    def load_summary(self) -> dict:
        data = self.load()
        return {
            "total_depots": len(data["depots"]),
            "total_customers": len(data["customers"]),
            "total_vehicles": len(data["vehicles"]),
            "total_demand": sum(data["demands"].values()),
            "vehicle_capacity": data["vehicle_capacity"],
        }