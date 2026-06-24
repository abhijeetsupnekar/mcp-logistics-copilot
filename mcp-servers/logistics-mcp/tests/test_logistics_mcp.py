import asyncio
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from mcp import ClientSession
from mcp.client.streamable_http import (
    streamable_http_client
)


LOGISTICS_MCP_URL = (
    "http://127.0.0.1:8000/mcp"
)


async def main():

    async with streamable_http_client(
        LOGISTICS_MCP_URL
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
                "shipment_eta_tool",
                {
                    "shipment_code": "SHP1003"
                }
            )

            print(result)


if __name__ == "__main__":
    asyncio.run(main())