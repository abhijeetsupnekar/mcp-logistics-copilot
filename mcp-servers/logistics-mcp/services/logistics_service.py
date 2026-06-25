import json

from src.mcp_client import LogisticsMCPClient


class LogisticsService:

    def __init__(self):

        self.client = LogisticsMCPClient()

    async def shipment_eta(
        self,
        shipment_code: str
    ):

        shipment_result = (
            await self.client.get_shipment_summary(
                shipment_code
            )
        )

        shipment_data = json.loads(
            shipment_result.content[0].text
        )

        shipment = shipment_data["shipment"]

        origin = shipment["Origin"]
        destination = shipment["Destination"]

        weather_result = (
            await self.client.current_weather(
                destination
            )
        )

        weather_data = json.loads(
            weather_result.content[0].text
        )

        maps_result = (
            await self.client.estimate_eta(
                origin,
                destination
            )
        )

        maps_data = json.loads(
            maps_result.content[0].text
        )

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

    async def shipment_status(
        self,
        shipment_code: str
    ):

        summary_result = (
            await self.client.get_shipment_summary(
                shipment_code
            )
        )
        print("========== SUMMARY RESULT ==========")
        print(type(summary_result))
        print(summary_result)

        print("========== CONTENT ==========")
        print(summary_result.content)

        print("========== TEXT ==========")
        print(type(summary_result.content[0].text))
        print(repr(summary_result.content[0].text))
        print("====================================")
        tracking_result = (
            await self.client.get_tracking(
                shipment_code
            )
        )

        summary_data = json.loads(
            summary_result.content[0].text
        )

        tracking_data = json.loads(
            tracking_result.content[0].text
        )

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
    async def delayed_shipments_alert(
        self
    ):

        delayed_result = (
            await self.client.get_delayed_shipments()
        )

        delayed_data = json.loads(
            delayed_result.content[0].text
        )

        shipment_code = delayed_data[
            "ShipmentCode"
        ]

        notification_result = (
            await self.client.send_notification(
                recipient="logistics-team@company.com",
                message=(
                    f"Shipment "
                    f"{shipment_code} "
                    f"is delayed."
                )
            )
        )

        return {
            "shipment_code": shipment_code,
            "notification_sent": True,
            "status": "success"
        }