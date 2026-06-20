from src.shipment_summary_service import get_shipment_summary


def register_shipment_summary_tools(mcp):

    @mcp.tool()
    def get_shipment_summary_tool(shipment_code: str):
        """
        Get complete shipment summary including
        shipment, vehicle, driver and tracking.
        """

        return get_shipment_summary(shipment_code)