import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.current_weather import (
    current_weather
)

result = current_weather(
    "Pune"
)

print(result)