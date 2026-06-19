import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.forecast_weather import (
    forecast_weather
)
result = forecast_weather("Pune")

print(result)