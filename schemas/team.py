from pydantic import BaseModel


class TeamCreate(BaseModel):
    team_name: str
    team_code: str
    description: str | None = None
    department_id: int


class TeamResponse(BaseModel):
    id: int
    team_name: str
    team_code: str
    description: str | None
    department_id: int
    is_active: bool

    class Config:
        from_attributes = True