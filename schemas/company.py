from pydantic import BaseModel


class CompanyCreate(BaseModel):
    company_name: str
    company_code: str
    email: str | None = None
    phone: str | None = None
    website: str | None = None
    address: str | None = None


class CompanyResponse(BaseModel):
    id: int
    company_name: str
    company_code: str
    email: str | None
    phone: str | None
    website: str | None
    address: str | None
    is_active: bool

    class Config:
        from_attributes = True