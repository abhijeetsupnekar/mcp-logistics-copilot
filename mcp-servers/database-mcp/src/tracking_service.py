from sqlalchemy import text

from src.database import get_connection


def get_shipment_tracking(shipment_code: str):

    with get_connection() as conn:

        query = text("""
            SELECT
                ShipmentCode,
                CurrentLocation,
                TrackingTime,
                Remarks
            FROM ShipmentTracking
            WHERE ShipmentCode = :shipment_code
            ORDER BY TrackingTime
        """)

        result = conn.execute(
            query,
            {"shipment_code": shipment_code}
        )

        rows = result.fetchall()

        if not rows:
            return {
                "message": f"No tracking found for {shipment_code}"
            }

        return [
            dict(row._mapping)
            for row in rows
        ]