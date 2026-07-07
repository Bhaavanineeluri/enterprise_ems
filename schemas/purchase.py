from pydantic import BaseModel


class PurchaseRequestCreate(BaseModel):
    request_no: str
    product_id: int
    vendor_id: int
    quantity: int


class PurchaseRequestResponse(BaseModel):
    id: int
    request_no: str
    status: str

    class Config:
        from_attributes = True


class PurchaseOrderCreate(BaseModel):
    po_number: str
    purchase_request_id: int


class PurchaseOrderResponse(BaseModel):
    id: int
    po_number: str
    status: str

    class Config:
        from_attributes = True