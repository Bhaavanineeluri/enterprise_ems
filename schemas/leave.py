from datetime import date

from pydantic import BaseModel, ConfigDict


class LeaveCreate(BaseModel):

    employee_id: int

    leave_type: str

    start_date: date

    end_date: date

    reason: str


class LeaveResponse(LeaveCreate):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    status: str