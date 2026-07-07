from pydantic import BaseModel, ConfigDict


class WorkflowCreate(BaseModel):

    name: str
    module: str
    description: str | None = None


class WorkflowResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    name: str
    module: str
    description: str | None
    is_active: bool