from pydantic import BaseModel, ConfigDict


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
    category: str | None = None
    brand: str | None = None
    price: float
    cost_price: float | None = None
    vendor_id: int | None = None
    company_id: int

    model_config = ConfigDict(from_attributes=True)