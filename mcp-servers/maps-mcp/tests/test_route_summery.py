from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from server import mcp
from tools.route_summary import route_by_address

result = route_by_address(
    "Pune",
    "Mumbai Airport"
)

print(result)