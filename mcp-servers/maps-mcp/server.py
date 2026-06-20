
from mcp.server.fastmcp import FastMCP
from tools.geocode import get_coordinates
from tools.traffic import get_route_traffic
from tools.route_summary import route_by_address
from tools.eta import estimate_eta




from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import TransportSecuritySettings

transport_security = TransportSecuritySettings(
    allowed_hosts=[
        "127.0.0.1:*",
        "localhost:*",
        "[::1]:*",
        "abhi-maps-mcp.azurewebsites.net"
    ],
    allowed_origins=[
        "http://127.0.0.1:*",
        "http://localhost:*",
        "http://[::1]:*",
        "https://abhi-maps-mcp.azurewebsites.net"
    ]
)

mcp = FastMCP(
    "Maps MCP",
    transport_security=transport_security
)

@mcp.tool()
def estimate_eta_tool(
    origin_address: str,
    destination_address: str
):
    return estimate_eta(
        origin_address,
        destination_address
    )

@mcp.tool()
def route_by_address_tool(
    origin_address: str,
    destination_address: str
):
    """
    Get route details using addresses.
    """

    return route_by_address(
        origin_address,
        destination_address
    )

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