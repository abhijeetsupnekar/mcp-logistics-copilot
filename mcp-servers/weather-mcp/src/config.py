from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.getenv(
    "WEATHER_API_KEY"
)

if not WEATHER_API_KEY:
    raise ValueError(
        "WEATHER_API_KEY is not set"
    )
