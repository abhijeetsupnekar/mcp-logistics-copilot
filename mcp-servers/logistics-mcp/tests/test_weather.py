import asyncio
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from src.mcp_client import LogisticsMCPClient


async def main():

    client = LogisticsMCPClient()

    result = await client.current_weather(
        "pune"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())