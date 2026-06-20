from src.shipment_service import get_shipment_details


def register_tools(mcp):

    @mcp.tool()
    def get_shipment_tool(shipment_code: str):
        """
        Get shipment details by shipment code.
        """
        return get_shipment_details(shipment_code)