from sqlalchemy import text

from src.database import get_connection


def get_driver_details(driver_code: str):

    with get_connection() as conn:

        query = text("""
            SELECT
                DriverID,
                DriverCode,
                DriverName,
                PhoneNumber,
                LicenseNumber,
                Status
            FROM Drivers
            WHERE DriverCode = :driver_code
        """)

        result = conn.execute(
            query,
            {"driver_code": driver_code}
        )

        row = result.fetchone()

        if row is None:
            return {
                "message": f"Driver {driver_code} not found"
            }

        return dict(row._mapping)