from tools.geocode import get_coordinates
from tools.traffic import get_route_traffic


def route_by_address(
    origin_address: str,
    destination_address: str
):

    origin = get_coordinates(origin_address)

    destination = get_coordinates(
        destination_address
    )

    if origin["status"] != "success":
        return origin

    if destination["status"] != "success":
        return destination

    traffic = get_route_traffic(
        origin["latitude"],
        origin["longitude"],
        destination["latitude"],
        destination["longitude"]
    )

    return {
        "origin": origin_address,
        "destination": destination_address,
        **traffic
    }