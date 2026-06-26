import logging
import os

from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

load_dotenv()

logger = logging.getLogger(__name__)


class LogisticsMCPClient:
    """
    Client responsible for communicating with all backend MCP servers.
    """

    def __init__(self):

        self.database_url = self._get_env("DATABASE_MCP_URL")
        self.maps_url = self._get_env("MAPS_MCP_URL")
        self.weather_url = self._get_env("WEATHER_MCP_URL")
        self.notification_url = self._get_env("NOTIFICATION_MCP_URL")

    @staticmethod
    def _get_env(variable_name: str) -> str:
        """
        Read and validate environment variables.
        """
        value = os.getenv(variable_name)

        if not value:
            raise ValueError(
                f"Missing required environment variable: {variable_name}"
            )

        return value

    async def _call_tool(
        self,
        mcp_url: str,
        tool_name: str,
        arguments: dict
    ):
        """
        Execute a tool on the specified MCP server.
        """

        try:

            async with streamable_http_client(
                mcp_url
            ) as (
                read_stream,
                write_stream,
                _
            ):

                async with ClientSession(
                    read_stream,
                    write_stream
                ) as session:

                    await session.initialize()

                    return await session.call_tool(
                        tool_name,
                        arguments
                    )

        except Exception:
            logger.exception(
                "Failed calling tool '%s' on MCP server '%s'",
                tool_name,
                mcp_url
            )
            raise

    # -------------------------
    # DATABASE MCP
    # -------------------------

    async def get_shipment(self, shipment_code: str):

        return await self._call_tool(
            self.database_url,
            "get_shipment_tool",
            {
                "shipment_code": shipment_code
            }
        )

    async def get_tracking(self, shipment_code: str):

        return await self._call_tool(
            self.database_url,
            "get_tracking_tool",
            {
                "shipment_code": shipment_code
            }
        )

    async def get_shipment_summary(self, shipment_code: str):

        return await self._call_tool(
            self.database_url,
            "get_shipment_summary_tool",
            {
                "shipment_code": shipment_code
            }
        )

    async def get_delayed_shipments(self):

        return await self._call_tool(
            self.database_url,
            "get_delayed_shipments_tool",
            {}
        )

    # -------------------------
    # MAPS MCP
    # -------------------------

    async def estimate_eta(
        self,
        origin_address: str,
        destination_address: str
    ):

        return await self._call_tool(
            self.maps_url,
            "estimate_eta_tool",
            {
                "origin_address": origin_address,
                "destination_address": destination_address
            }
        )

    async def route_by_address(
        self,
        origin_address: str,
        destination_address: str
    ):

        return await self._call_tool(
            self.maps_url,
            "route_by_address_tool",
            {
                "origin_address": origin_address,
                "destination_address": destination_address
            }
        )

    # -------------------------
    # WEATHER MCP
    # -------------------------

    async def current_weather(self, city: str):

        return await self._call_tool(
            self.weather_url,
            "current_weather_tool",
            {
                "city": city
            }
        )

    async def forecast_weather(self, city: str):

        return await self._call_tool(
            self.weather_url,
            "forecast_weather_tool",
            {
                "city": city
            }
        )

    # -------------------------
    # NOTIFICATION MCP
    # -------------------------

    async def send_notification(
        self,
        recipient: str,
        message: str
    ):

        return await self._call_tool(
            self.notification_url,
            "send_notification_tool",
            {
                "recipient": recipient,
                "message": message
            }
        )