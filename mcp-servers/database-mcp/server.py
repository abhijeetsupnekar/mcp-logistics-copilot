from mcp.server.fastmcp import FastMCP
from tools.shipment_tool import register_tools
from tools.vehicle_tools import register_vehicle_tools
from tools.driver_tools import register_driver_tools
from tools.tracking_tools import register_tracking_tools
from tools.shipment_summary_tools import register_shipment_summary_tools
from tools.delayed_shipment_tools import (
    register_delayed_shipment_tools
)
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import TransportSecuritySettings
mcp = FastMCP(
    "Database MCP",
    host="0.0.0.0",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "127.0.0.1:*",
            "localhost:*",
            "[::1]:*",
            "abhi-database-mcp.azurewebsites.net"
        ],
        allowed_origins=[
            "http://127.0.0.1:*",
            "http://localhost:*",
            "http://[::1]:*",
            "https://abhi-database-mcp.azurewebsites.net"
        ]
    )
)

register_tools(mcp)
register_tracking_tools(mcp)
register_shipment_summary_tools(mcp)
register_delayed_shipment_tools(mcp)
register_vehicle_tools(mcp)
register_driver_tools(mcp)

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )