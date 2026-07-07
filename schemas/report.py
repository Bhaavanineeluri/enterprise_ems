from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReportCreate(BaseModel):

    report_name: str

    report_type: str

    generated_by: str


class ReportResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    report_name: str

    report_type: str

    generated_by: str

    created_at: datetime