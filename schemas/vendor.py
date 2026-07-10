from datetime import date

from pydantic import BaseModel


class VendorCreate(BaseModel):
    vendor_code: str
    name: str
    email: str | None = None
    phone: str | None = None
    contract_number: str | None = None
    contract_start_date: date | None = None
    contract_end_date: date | None = None
    rating: int | None = 0
    remarks: str | None = None
    is_compliant: bool = True


class VendorResponse(BaseModel):
    id: int
    vendor_code: str
    name: str
    email: str | None = None
    phone: str | None = None
    contract_number: str | None = None
    contract_start_date: date | None = None
    contract_end_date: date | None = None
    rating: int | None = 0
    remarks: str | None = None
    is_compliant: bool = True

    class Config:
        from_attributes = True


class VendorEvaluation(BaseModel):
    rating: int
    remarks: str