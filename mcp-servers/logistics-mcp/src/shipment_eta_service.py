from datetime import datetime, timedelta


def calculate_eta(
        shipment_data: dict,
        route_data: dict
):
    duration_hours = route_data["duration_hours"]

    eta_time = (
        datetime.now()
        + timedelta(hours=duration_hours)
    )

    return {
        "shipment_id": shipment_data["shipment_id"],
        "origin": shipment_data["origin"],
        "destination": shipment_data["destination"],
        "distance_km": route_data["distance_km"],
        "estimated_arrival": eta_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }