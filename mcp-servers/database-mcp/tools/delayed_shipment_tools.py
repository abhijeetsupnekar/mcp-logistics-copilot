from src.delayed_shipment_service import get_delayed_shipments


def register_delayed_shipment_tools(mcp):

    @mcp.tool()
    def get_delayed_shipments_tool():
        """
        Get all delayed shipments.
        """

        return get_delayed_shipments()