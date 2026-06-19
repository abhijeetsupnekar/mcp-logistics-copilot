import requests
from src.config import WEATHER_API_KEY



def get_weather_forecast(city: str):

    url = (
        "https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        "&units=metric"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    return response.json()

def get_current_weather(city: str):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        "&units=metric"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    return response.json()