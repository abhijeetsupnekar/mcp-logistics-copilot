from mcp.server.fastmcp import FastMCP

from tools.shipment_status_tool import (
    shipment_status_tool
)
from tools.shipment_eta_tool import (
    get_shipment_eta_tool
)

mcp = FastMCP(
    "Logistics MCP"
)
@mcp.tool()
def get_shipment_eta(
        shipment_id: str
):
    """
    Get shipment ETA using
    Database MCP + Maps MCP
    """
    return get_shipment_eta_tool(
        shipment_id
    )

@mcp.tool()
def get_shipment_status_tool(
    shipment_code: str
):
    """
    Get complete shipment status.
    """

    return shipment_status_tool(
        shipment_code
    )


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )