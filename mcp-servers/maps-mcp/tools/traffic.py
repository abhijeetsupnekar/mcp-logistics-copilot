from src.google_maps_client import get_route_info


def get_route_traffic(
    origin_lat: float,
    origin_lng: float,
    dest_lat: float,
    dest_lng: float
):

    data = get_route_info(
        origin_lat,
        origin_lng,
        dest_lat,
        dest_lng
    )

    route = data["routes"][0]

    distance_km = round(
        route["distanceMeters"] / 1000,
        2
    )

    duration_seconds = int(
        route["duration"].replace("s", "")
    )

    duration_minutes = round(
        duration_seconds / 60,
        2
    )

    route_summary = route.get(
        "description",
        "Unknown Route"
    )

    return {
        "status": "success",
        "distance_km": distance_km,
        "duration_minutes": duration_minutes,
        "route_summary": route_summary
    }