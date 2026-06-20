from src.tracking_service import get_shipment_tracking


def register_tracking_tools(mcp):

    @mcp.tool()
    def get_tracking_tool(shipment_code: str):
        """
        Get shipment tracking details.
        """

        return get_shipment_tracking(shipment_code)