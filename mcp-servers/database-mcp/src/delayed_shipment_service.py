from sqlalchemy import text

from src.database import get_connection


def get_delayed_shipments():

    with get_connection() as conn:

        query = text("""
            SELECT
                ShipmentCode,
                Origin,
                Destination,
                Status,
                VehicleCode,
                ExpectedDelivery
            FROM Shipments
            WHERE Status = 'Delayed'
            ORDER BY ExpectedDelivery
        """)

        result = conn.execute(query)

        rows = result.fetchall()

        return [
            dict(row._mapping)
            for row in rows
        ]