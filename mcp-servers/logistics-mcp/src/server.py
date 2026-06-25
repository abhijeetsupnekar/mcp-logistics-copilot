from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from mcp.server.fastmcp import FastMCP
from services.logistics_service import LogisticsService


from mcp.server.fastmcp.server import TransportSecuritySettings

mcp = FastMCP(
    "Logistics MCP",
    host="0.0.0.0",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "127.0.0.1:*",
            "localhost:*",
            "[::1]:*",
            "abhi-logistics-mcp-g8evfbgxbqdudfau.swedencentral-01.azurewebsites.net"
        ],
        allowed_origins=[
            "http://127.0.0.1:*",
            "http://localhost:*",
            "http://[::1]:*",
            "https://abhi-logistics-mcp-g8evfbgxbqdudfau.swedencentral-01.azurewebsites.net"
        ]
    )
)

service = LogisticsService()


@mcp.tool()
async def shipment_status_tool(shipment_code: str):
    """
    Get shipment status, driver and tracking details.
    """
    return await service.shipment_status(shipment_code)


@mcp.tool()
async def delayed_shipments_alert_tool():
    """
    Send notifications for delayed shipments.
    """
    return await service.delayed_shipments_alert()


@mcp.tool()
async def shipment_eta_tool(shipment_code: str):
    """
    Get shipment ETA using:
    Database MCP + Maps MCP + Weather MCP
    """
    return await service.shipment_eta(shipment_code)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )