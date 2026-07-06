from pydantic import BaseModel


class UserAssignment(BaseModel):
    user_id: int
    company_id: int | None = None
    branch_id: int | None = None
    department_id: int | None = None
    team_id: int | None = None