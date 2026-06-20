from pathlib import Path
import sys

ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.append(str(ROOT))

from shipment_eta_service import (
    get_shipment_eta
)

result = get_shipment_eta(
    "SHP1001"
)

print(result)