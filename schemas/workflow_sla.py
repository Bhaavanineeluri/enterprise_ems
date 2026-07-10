from pydantic import BaseModel, ConfigDict


class WorkflowSLACreate(BaseModel):

    workflow_id: int

    approval_level: int = 1

    allowed_hours: int

    action: str = "ESCALATE"



class WorkflowSLAResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    workflow_id: int

    approval_level: int

    allowed_hours: int

    action: str