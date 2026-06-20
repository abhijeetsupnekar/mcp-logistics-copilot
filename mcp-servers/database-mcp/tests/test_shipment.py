import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)
from src.shipment_service import get_shipment_details

result = get_shipment_details("SHP1001")

print(result)