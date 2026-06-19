from src.weather_client import get_weather_forecast


def forecast_weather(city: str):

    data = get_weather_forecast(city)

    forecasts = []

    for item in data["list"][:5]:

        forecasts.append({
            "time": item["dt_txt"],
            "temperature_c": item["main"]["temp"],
            "condition": item["weather"][0]["description"]
        })

    return {
        "status": "success",
        "city": city,
        "forecast": forecasts
    }