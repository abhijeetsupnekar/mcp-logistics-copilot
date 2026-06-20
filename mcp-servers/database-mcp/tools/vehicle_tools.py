from src.vehicle_service import get_vehicle_details


def register_vehicle_tools(mcp):

    @mcp.tool()
    def get_vehicle_tool(vehicle_code: str):
        """
        Get vehicle details by vehicle code.
        """
        return get_vehicle_details(vehicle_code)