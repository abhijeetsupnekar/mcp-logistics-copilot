from src.shipment_status_service import (
    get_shipment_status
)


def shipment_status_tool(
    shipment_code: str
):
    return get_shipment_status(
        shipment_code
    )