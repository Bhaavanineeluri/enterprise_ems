from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    department_name: str
    department_code: str
    description: str | None = None
    branch_id: int


class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    department_code: str
    description: str | None
    branch_id: int
    is_active: bool

    class Config:
        from_attributes = True