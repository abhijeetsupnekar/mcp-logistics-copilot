import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)
from src.vehicle_service import get_vehicle_details

result = get_vehicle_details("VH001")

print(result)