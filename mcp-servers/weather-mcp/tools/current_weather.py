from src.weather_client import get_current_weather


def current_weather(city: str):

    data = get_current_weather(city)

    return {
        "status": "success",
        "city": data["name"],
        "temperature_c": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "wind_kph": round(
            data["wind"]["speed"] * 3.6,
            2
        )
    }