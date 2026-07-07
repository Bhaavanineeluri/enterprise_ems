from pydantic import BaseModel
from typing import Optional


# ----------------------------
# CREATE GOODS RECEIPT
# ----------------------------
class GoodsReceiptCreate(BaseModel):
    grn_number: str
    purchase_order_id: int
    product_id: int
    received_quantity: int
    received_by: int
    remarks: Optional[str] = None


# ----------------------------
# RESPONSE
# ----------------------------
class GoodsReceiptResponse(BaseModel):
    id: int
    grn_number: str
    purchase_order_id: int
    product_id: int
    received_quantity: int
    received_by: int
    remarks: Optional[str]

    class Config:
        from_attributes = True