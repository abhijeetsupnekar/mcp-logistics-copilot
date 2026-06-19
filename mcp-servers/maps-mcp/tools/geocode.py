from src.google_maps_client import geocode_address


def get_coordinates(address: str):

    data = geocode_address(address)

    if data.get("status") == "REQUEST_DENIED":
        return {
            "status": "error",
            "message": data.get(
                "error_message",
                "API access denied"
            )
        }

    if not data.get("results"):
        return {
            "status": "error",
            "message": "Address not found"
        }

    location = (
        data["results"][0]
        ["geometry"]
        ["location"]
    )

    return {
        "status": "success",
        "address": address,
        "latitude": location["lat"],
        "longitude": location["lng"]
    }