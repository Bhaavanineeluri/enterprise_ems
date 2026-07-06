from pydantic import BaseModel


class VendorCreate(BaseModel):
    vendor_code: str
    name: str
    email: str | None = None
    phone: str | None = None


class VendorResponse(BaseModel):
    id: int
    vendor_code: str
    name: str

    class Config:
        from_attributes = True