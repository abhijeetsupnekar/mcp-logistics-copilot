import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from server import mcp

print("Name:", mcp.name)

for tool in mcp._tool_manager.list_tools():
    print("Tool:", tool.name)