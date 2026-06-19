from datetime import datetime, timedelta

from tools.route_summary import route_by_address


def estimate_eta(
    origin_address: str,
    destination_address: str
):
    route = route_by_address(
        origin_address,
        destination_address
    )

    if route["status"] != "success":
        return route

    duration_minutes = route["duration_minutes"]

    departure_time = datetime.now()

    arrival_time = departure_time + timedelta(
        minutes=duration_minutes
    )

    return {
        "status": "success",
        "origin": origin_address,
        "destination": destination_address,
        "distance_km": route["distance_km"],
        "duration_minutes": duration_minutes,
        "departure_time": departure_time.strftime(
            "%Y-%m-%d %H:%M"
        ),
        "estimated_arrival": arrival_time.strftime(
            "%Y-%m-%d %H:%M"
        )
    }