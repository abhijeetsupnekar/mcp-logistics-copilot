from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv(
    "GOOGLE_MAPS_API_KEY"
)

if not GOOGLE_MAPS_API_KEY:
    raise ValueError(
        "GOOGLE_MAPS_API_KEY is missing."
    )
