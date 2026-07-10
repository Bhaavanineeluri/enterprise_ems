from datetime import date
from pydantic import BaseModel, ConfigDict


class AttendanceCreate(BaseModel):

    employee_id: int

    attendance_date: date

    check_in: str

    check_out: str

    status: str = "Present"


class AttendanceResponse(AttendanceCreate):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int