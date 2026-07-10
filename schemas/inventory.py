from typing import Literal

from pydantic import BaseModel, ConfigDict


class InventoryUpdate(BaseModel):
    product_id: int
    quantity: int


class InventoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    quantity: int


# =====================================================
# STOCK ADJUSTMENT
# =====================================================

class StockAdjustmentRequest(BaseModel):

    inventory_id: int

    adjustment_type: Literal["IN", "OUT"]

    quantity: int

    reason: str

    created_by: int


class StockAdjustmentResponse(BaseModel):

    message: str

    current_quantity: int