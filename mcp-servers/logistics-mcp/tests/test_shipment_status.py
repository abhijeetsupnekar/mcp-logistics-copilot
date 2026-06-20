import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.append(
    str(ROOT)
)

from src.shipment_status_service import (
    get_shipment_status
)

result = get_shipment_status(
    "SHP1001"
)

print(result)