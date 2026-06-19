from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from server import mcp

print("Server:", mcp)
print("Name:", mcp.name)

for tool in mcp._tool_manager.list_tools():
    print("Tool:", tool.name)