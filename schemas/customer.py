from pydantic import BaseModel
from typing import Optional


class CustomerCreate(BaseModel):
    user_id: int
    customer_code: str |None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None


class CustomerResponse(BaseModel):
    id: int
    user_id: int
    customer_code: str | None = None
    address: str | None

    class Config:
        from_attributes = True


class CustomerUpdate(BaseModel):
    customer_code: Optional[str] = None

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None