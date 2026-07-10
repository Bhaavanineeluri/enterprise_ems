from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class EmployeeCreate(BaseModel):

    user_id: int

    employee_code: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None


class EmployeeUpdate(BaseModel):

    employee_code: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None

    class Config:
        from_attributes = True


class EmployeeSelfUpdate(BaseModel):

    designation: Optional[str] = None


class EmployeeResponse(BaseModel):

    id: int
    user_id: int

    employee_code: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True