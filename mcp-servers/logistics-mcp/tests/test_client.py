import asyncio
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


from src.mcp_client import (
    get_shipment_summary
)

result = asyncio.run(
    get_shipment_summary(
        "SHP1003"
    )
)

print(result)