from mcp.server.fastmcp import FastMCP

from tools.current_weather import current_weather
from tools.forecast_weather import forecast_weather

mcp = FastMCP("Weather MCP")


@mcp.tool()
def current_weather_tool(city: str):
    """
    Get current weather.
    """
    return current_weather(city)


@mcp.tool()
def forecast_weather_tool(city: str):
    """
    Get weather forecast.
    """
    return forecast_weather(city)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")