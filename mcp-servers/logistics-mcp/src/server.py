from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from mcp.server.fastmcp import FastMCP
from services.logistics_service import LogisticsService


mcp = FastMCP("Logistics MCP")

service = LogisticsService()


@mcp.tool()
async def shipment_status_tool(shipment_code: str):
    return await service.shipment_status(shipment_code)


@mcp.tool()
async def delayed_shipments_alert_tool():
    return await service.delayed_shipments_alert()


@mcp.tool()
async def shipment_eta_tool(shipment_code: str):
    return await service.shipment_eta(shipment_code)


# IMPORTANT
app = mcp.streamable_http_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )