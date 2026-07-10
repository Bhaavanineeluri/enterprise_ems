from pydantic import BaseModel


class TenantCreate(BaseModel):

    tenant_name: str
    tenant_code: str


class TenantResponse(BaseModel):

    id: int
    tenant_name: str
    tenant_code: str
    status: bool

    class Config:
        from_attributes = True