import os

from dotenv import load_dotenv



load_dotenv()
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


import json


def parse_result(result):

    return json.loads(
        result.content[0].text
    )

class LogisticsMCPClient:

    def __init__(self):

        self.database_url = os.getenv(
            "DATABASE_MCP_URL"
        )

        self.maps_url = os.getenv(
            "MAPS_MCP_URL"
        )

        self.weather_url = os.getenv(
            "WEATHER_MCP_URL"
        )

        self.notification_url = os.getenv(
            "NOTIFICATION_MCP_URL"
        )

    async def _call_tool(
        self,
        mcp_url: str,
        tool_name: str,
        arguments: dict
    ):

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

                result = await session.call_tool(
                    tool_name,
                    arguments
                )

                return result

    # -------------------------
    # DATABASE MCP
    # -------------------------

    async def get_shipment(
        self,
        shipment_code: str
    ):

        return await self._call_tool(
            self.database_url,
            "get_shipment_tool",
            {
                "shipment_code": shipment_code
            }
        )

    async def get_tracking(
        self,
        shipment_code: str
    ):

        return await self._call_tool(
            self.database_url,
            "get_tracking_tool",
            {
                "shipment_code": shipment_code
            }
        )

    async def get_shipment_summary(
        self,
        shipment_code: str
    ):

        return await self._call_tool(
            self.database_url,
            "get_shipment_summary_tool",
            {
                "shipment_code": shipment_code
            }
        )

    async def get_delayed_shipments(
        self
    ):

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

    async def current_weather(
        self,
        city: str
    ):

        return await self._call_tool(
            self.weather_url,
            "current_weather_tool",
            {
                "city": city
            }
        )

    async def forecast_weather(
        self,
        city: str
    ):

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