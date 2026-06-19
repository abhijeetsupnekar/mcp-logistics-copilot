import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.geocode import get_coordinates

result = get_coordinates(
    "Hinjewadi Pune"
)

print(result)