from sqlalchemy import text

from src.database import get_connection


def get_shipment_details(shipment_code: str):

    with get_connection() as conn:

        query = text("""
            SELECT
                ShipmentID,
                ShipmentCode,
                Origin,
                Destination,
                Status,
                VehicleCode,
                ExpectedDelivery
            FROM Shipments
            WHERE ShipmentCode = :shipment_code
        """)

        result = conn.execute(
            query,
            {"shipment_code": shipment_code}
        )

        row = result.fetchone()

        if row is None:
            return {
                "message": f"Shipment {shipment_code} not found"
            }

        return dict(row._mapping)