from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import TransportSecuritySettings

from tools.current_weather import current_weather
from tools.forecast_weather import forecast_weather

mcp = FastMCP(
    "Weather MCP",
    host="0.0.0.0",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "127.0.0.1:*",
            "localhost:*",
            "[::1]:*",
            "abhi-weather-mcp.azurewebsites.net"
        ],
        allowed_origins=[
            "http://127.0.0.1:*",
            "http://localhost:*",
            "http://[::1]:*",
            "https://abhi-weather-mcp.azurewebsites.net"
        ]
    )
)

@mcp.tool()
def current_weather_tool(city: str):
    return current_weather(city)

@mcp.tool()
def forecast_weather_tool(city: str):
    return forecast_weather(city)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")