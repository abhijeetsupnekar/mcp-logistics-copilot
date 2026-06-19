import requests

from src.config import GOOGLE_MAPS_API_KEY


def geocode_address(address: str):

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    response = requests.get(
        url,
        params={
            "address": address,
            "key": GOOGLE_MAPS_API_KEY
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def get_route_info(
    origin_lat: float,
    origin_lng: float,
    dest_lat: float,
    dest_lng: float
):
    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask":
            "routes.distanceMeters,"
            "routes.duration,"
            "routes.description"
    }

    payload = {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": origin_lat,
                    "longitude": origin_lng
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": dest_lat,
                    "longitude": dest_lng
                }
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE"
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    return response.json()

def geocode_address(
    address: str
):
    url = (
        "https://maps.googleapis.com/maps/api/geocode/json"
    )

    response = requests.get(
        url,
        params={
            "address": address,
            "key": GOOGLE_MAPS_API_KEY
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()