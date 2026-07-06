from pydantic import BaseModel


class CustomerCreate(BaseModel):
    user_id: int
    customer_code: str
    company_name: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None


class CustomerResponse(BaseModel):
    id: int
    user_id: int
    customer_code: str
    company_name: str | None
    address: str | None

    class Config:
        from_attributes = True