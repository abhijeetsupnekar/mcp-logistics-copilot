from services.logistics_service import (
    LogisticsService
)

service = LogisticsService()


async def shipment_eta_tool(
    shipment_code: str
):

    return await service.shipment_eta(
        shipment_code
    )