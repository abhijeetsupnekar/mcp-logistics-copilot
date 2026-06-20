from pathlib import Path
import sys
from src.shipment_summary_service import (
    get_shipment_summary
)
ROOT = Path(__file__).resolve().parent.parent.parent

database_mcp = ROOT / "database-mcp"

sys.path.insert(0, str(database_mcp))

if "src" in sys.modules:
    del sys.modules["src"]




def get_shipment_status(
    shipment_code: str
):
    data = get_shipment_summary(
        shipment_code
    )

    if not data:
        return {
            "status": "Not Found"
        }

    return {
        "shipment_code": shipment_code,
        "status": data["shipment"]["Status"]
    }