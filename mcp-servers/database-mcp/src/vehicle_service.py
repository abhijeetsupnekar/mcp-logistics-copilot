from sqlalchemy import text

from src.database import get_connection


def get_vehicle_details(vehicle_code: str):

    with get_connection() as conn:

        query = text("""
            SELECT
                VehicleID,
                VehicleCode,
                VehicleNumber,
                VehicleType,
                Capacity,
                DriverCode,
                CurrentLocation,
                Status
            FROM Vehicles
            WHERE VehicleCode = :vehicle_code
        """)

        result = conn.execute(
            query,
            {"vehicle_code": vehicle_code}
        )

        row = result.fetchone()

        if row is None:
            return {
                "message": f"Vehicle {vehicle_code} not found"
            }

        return dict(row._mapping)