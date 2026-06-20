from src.shipment_service import get_shipment_details
from src.vehicle_service import get_vehicle_details
from src.driver_service import get_driver_details
from src.tracking_service import get_shipment_tracking


def get_shipment_summary(shipment_code: str):

    shipment = get_shipment_details(shipment_code)

    if "message" in shipment:
        return shipment

    vehicle_code = shipment["VehicleCode"]

    vehicle = get_vehicle_details(vehicle_code)

    driver_code = vehicle["DriverCode"]

    driver = get_driver_details(driver_code)

    tracking = get_shipment_tracking(shipment_code)

    return {
        "shipment": shipment,
        "vehicle": vehicle,
        "driver": driver,
        "tracking": tracking
    }