from mcp.server.fastmcp import FastMCP
from tools.shipment_tool import register_tools
from tools.vehicle_tools import register_vehicle_tools
from tools.driver_tools import register_driver_tools
from tools.tracking_tools import register_tracking_tools
from tools.shipment_summary_tools import register_shipment_summary_tools
from tools.delayed_shipment_tools import (
    register_delayed_shipment_tools
)

mcp = FastMCP("Database MCP")

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