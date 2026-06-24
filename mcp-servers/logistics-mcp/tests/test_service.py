import asyncio
import sys

from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.logistics_service import (
    LogisticsService
)


async def main():

    service = LogisticsService()

    result = await service.shipment_eta(
        "SHP1003"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())