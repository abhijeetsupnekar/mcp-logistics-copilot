from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# Database MCP
database_mcp = ROOT / "database-mcp"

# Maps MCP
maps_mcp = ROOT / "maps-mcp"

sys.path.insert(0, str(database_mcp))
from src.shipment_summary_service import (
    get_shipment_summary
)

sys.path.pop(0)

sys.path.insert(0, str(maps_mcp))
from tools.eta import estimate_eta

sys.path.pop(0)


def get_shipment_eta(shipment_code: str):

    shipment_summary = get_shipment_summary(
        shipment_code
    )

    tracking = shipment_summary["tracking"]

    latest_tracking = tracking[-1]

    current_location = latest_tracking[
        "CurrentLocation"
    ]

    destination = shipment_summary[
        "shipment"
    ]["Destination"]

    eta = estimate_eta(
        current_location,
        destination
    )

    return {
        "shipment_code": shipment_code,
        "current_location": current_location,
        "destination": destination,
        **eta
    }