from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# -------------------------
# DATABASE MCP
# -------------------------

database_mcp = ROOT / "database-mcp"

sys.path.insert(0, str(database_mcp))

from src.shipment_summary_service import (
    get_shipment_summary
)

sys.path.pop(0)

print("Database Import Successful")

result = get_shipment_summary("SHP1001")

print(result)

# -------------------------
# MAPS MCP
# -------------------------

maps_mcp = ROOT / "maps-mcp"

sys.path.insert(0, str(maps_mcp))
sys.path.insert(0, str(maps_mcp / "src"))
sys.path.insert(0, str(maps_mcp / "tools"))

from tools.eta import estimate_eta

eta = estimate_eta(
    "Khalapur",
    "Mumbai"
)

print("\nETA RESULT")
print(eta)