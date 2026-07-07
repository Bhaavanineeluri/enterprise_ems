from pydantic import BaseModel, ConfigDict
from typing import Optional


# =====================================================
# SHIPMENT
# =====================================================

class ShipmentCreate(BaseModel):
    shipment_number: str
    sales_order_id: int
    shipped_by: int
    courier_name: str
    tracking_number: str


class ShipmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    shipment_number: str
    sales_order_id: int
    shipped_by: int
    courier_name: str
    tracking_number: str
    status: str


# =====================================================
# DELIVERY
# =====================================================

class DeliveryCreate(BaseModel):
    delivery_number: str
    shipment_id: int
    delivered_to: int
    delivered_by: int
    received_by: str
    remarks: Optional[str] = None


class DeliveryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    delivery_number: str
    shipment_id: int
    delivered_to: int
    delivered_by: int
    delivery_status: str
    received_by: str
    remarks: Optional[str]