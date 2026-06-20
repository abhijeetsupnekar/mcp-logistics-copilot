
from src.shipment_eta_service import (
    calculate_eta
)
from clients.database_client import (
    get_shipment
)

from clients.maps_client import (
    get_route_info
)


def get_shipment_eta_tool(
        shipment_id: str
):
    shipment = get_shipment(
        shipment_id
    )

    route = get_route_info(
        shipment["origin"],
        shipment["destination"]
    )

    result = calculate_eta(
        shipment,
        route
    )

    return result