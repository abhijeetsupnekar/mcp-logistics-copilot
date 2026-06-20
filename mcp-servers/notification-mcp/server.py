from mcp.server.fastmcp import FastMCP

from tools.send_notification import send_notification

mcp = FastMCP("Notification MCP")


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