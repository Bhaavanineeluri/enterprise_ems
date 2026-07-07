from pydantic import BaseModel, ConfigDict


class ApprovalCreate(BaseModel):

    workflow_id: int
    requested_by: int
    level: int = 1


class ApprovalUpdate(BaseModel):

    status: str
    approved_by: int | None = None
    remarks: str | None = None


class ApprovalResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    workflow_id: int
    requested_by: int
    approved_by: int | None
    status: str
    level: int
    remarks: str | None