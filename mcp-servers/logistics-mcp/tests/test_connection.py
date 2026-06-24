import asyncio
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from src.mcp_client import (
    test_database_connection
)


result = asyncio.run(
    test_database_connection()
)

print(result)