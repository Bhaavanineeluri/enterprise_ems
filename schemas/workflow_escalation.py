from pydantic import BaseModel, ConfigDict


class WorkflowEscalationCreate(BaseModel):

    workflow_id: int

    level: int = 1

    after_hours: int

    escalate_to: str



class WorkflowEscalationResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int

    workflow_id: int

    level: int

    after_hours: int

    escalate_to: str

    status: str