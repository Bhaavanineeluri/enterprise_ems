from pydantic import BaseModel


class BranchCreate(BaseModel):
    branch_name: str
    branch_code: str
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    company_id: int


class BranchResponse(BaseModel):
    id: int
    branch_name: str
    branch_code: str
    email: str | None
    phone: str | None
    address: str | None
    company_id: int
    is_active: bool

    class Config:
        from_attributes = True