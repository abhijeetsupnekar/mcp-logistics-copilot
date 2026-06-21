from mcp.server.fastmcp import FastMCP

from tools.send_notification import send_notification

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import TransportSecuritySettings

transport_security = TransportSecuritySettings(
    allowed_hosts=[
        "127.0.0.1:*",
        "localhost:*",
        "[::1]:*",
        "abhi-notification-mcp.azurewebsites.net"
    ],
    allowed_origins=[
        "http://127.0.0.1:*",
        "http://localhost:*",
        "http://[::1]:*",
        "https://abhi-notification-mcp.azurewebsites.net"
    ]
)

mcp = FastMCP(
    "Notification MCP",
    transport_security=transport_security
)






@mcp.tool()
def send_notification_tool(
    recipient: str,
    message: str
):
    """
    Send a notification.
    """
    return send_notification(
        recipient,
        message
    )


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )