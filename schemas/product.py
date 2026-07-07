from pydantic import BaseModel


class ProductCreate(BaseModel):
    product_code: str
    name: str
    category: str | None = None
    brand: str | None = None
    price: float
    cost_price: float | None = None
    vendor_id: int | None = None


class ProductResponse(BaseModel):
    id: int
    product_code: str
    name: str
    price: float

    class Config:
        from_attributes = True