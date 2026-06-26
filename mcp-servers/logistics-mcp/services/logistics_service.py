import json
import logging
from typing import Any

from src.mcp_client import LogisticsMCPClient

logger = logging.getLogger(__name__)


class LogisticsService:

    def __init__(self):
        self.client = LogisticsMCPClient()

    def _parse_response(self, response: Any) -> dict:
        """
        Parse and validate MCP response.
        """
        if not response or not response.content:
            raise ValueError("Received empty response from MCP server.")

        try:
            return json.loads(response.content[0].text)
        except (json.JSONDecodeError, IndexError, AttributeError) as ex:
            logger.exception("Failed to parse MCP response.")
            raise ValueError("Invalid response received from MCP server.") from ex

    async def shipment_eta(
        self,
        shipment_code: str
    ) -> dict:

        try:
            shipment_result = await self.client.get_shipment_summary(
                shipment_code
            )

            shipment_data = self._parse_response(shipment_result)
            shipment = shipment_data["shipment"]

            origin = shipment["Origin"]
            destination = shipment["Destination"]

            weather_result = await self.client.current_weather(
                destination
            )
            weather_data = self._parse_response(weather_result)

            maps_result = await self.client.estimate_eta(
                origin,
                destination
            )
            maps_data = self._parse_response(maps_result)

            return {
                "shipment_code": shipment_code,
                "origin": origin,
                "destination": destination,
                "shipment_status": shipment["Status"],
                "weather": weather_data["condition"],
                "temperature_c": weather_data["temperature_c"],
                "distance_km": maps_data["distance_km"],
                "duration_minutes": maps_data["duration_minutes"],
                "estimated_arrival": maps_data["estimated_arrival"]
            }

        except Exception:
            logger.exception(
                "Failed to fetch ETA for shipment %s",
                shipment_code
            )
            raise

    async def shipment_status(
        self,
        shipment_code: str
    ) -> dict:

        try:
            summary_result = await self.client.get_shipment_summary(
                shipment_code
            )

            tracking_result = await self.client.get_tracking(
                shipment_code
            )

            summary_data = self._parse_response(summary_result)
            tracking_data = self._parse_response(tracking_result)

            shipment = summary_data["shipment"]
            vehicle = summary_data["vehicle"]
            driver = summary_data["driver"]

            return {
                "shipment_code": shipment["ShipmentCode"],
                "shipment_status": shipment["Status"],
                "origin": shipment["Origin"],
                "destination": shipment["Destination"],
                "driver_name": driver["DriverName"],
                "vehicle_number": vehicle["VehicleNumber"],
                "tracking": tracking_data
            }

        except Exception:
            logger.exception(
                "Failed to fetch shipment status for %s",
                shipment_code
            )
            raise

    async def delayed_shipments_alert(self) -> dict:

        try:
            delayed_result = await self.client.get_delayed_shipments()

            delayed_data = self._parse_response(delayed_result)

            shipment_code = delayed_data["ShipmentCode"]

            notification_result = await self.client.send_notification(
                recipient="logistics-team@company.com",
                message=f"Shipment {shipment_code} is delayed."
            )

            notification_data = self._parse_response(notification_result)

            notification_sent = notification_data.get(
                "status",
                ""
            ).lower() == "success"

            return {
                "shipment_code": shipment_code,
                "notification_sent": notification_sent,
                "notification_response": notification_data
            }

        except Exception:
            logger.exception(
                "Failed to process delayed shipment notification."
            )
            raise