from pydantic import BaseModel, ConfigDict
from typing import Optional



class ApprovalCreate(BaseModel):

    workflow_id: int

    request_id: int

    approver_id: int

    approval_level: int = 1



class ApprovalUpdate(BaseModel):

    status: str

    remarks: Optional[str] = None



class ApprovalResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int

    workflow_id: int

    request_id: int

    approver_id: int

    approval_level: int

    status: str

    remarks: Optional[str]