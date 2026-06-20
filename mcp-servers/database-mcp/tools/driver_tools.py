from src.driver_service import get_driver_details


def register_driver_tools(mcp):

    @mcp.tool()
    def get_driver_tool(driver_code: str):
        """
        Get driver details by driver code.
        """
        return get_driver_details(driver_code)