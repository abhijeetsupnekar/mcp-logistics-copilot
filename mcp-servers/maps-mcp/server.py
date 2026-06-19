
from mcp.server.fastmcp import FastMCP

from tools.geocode import get_coordinates
from tools.traffic import get_route_traffic

mcp = FastMCP("Maps MCP")


@mcp.tool()
def hello(name: str):
    """
    Simple test tool.
    """
    return f"Hello {name}"


@mcp.tool()
def geocode(address: str):
    """
    Convert address into coordinates.
    """
    return get_coordinates(address)


@mcp.tool()
def route_traffic(
    origin_lat: float,
    origin_lng: float,
    dest_lat: float,
    dest_lng: float
):
    """
    Get traffic information between two coordinates.
    """
    return get_route_traffic(
        origin_lat,
        origin_lng,
        dest_lat,
        dest_lng
    )


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )