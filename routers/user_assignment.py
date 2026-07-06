from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_assignment import UserAssignment
from services.user_assignment import assign_user

router = APIRouter(prefix="/assign", tags=["User Assignment"])


@router.post("/")
def assign(data: UserAssignment, db: Session = Depends(get_db)):
    return assign_user(
        db,
        user_id=data.user_id,
        company_id=data.company_id,
        branch_id=data.branch_id,
        department_id=data.department_id,
        team_id=data.team_id
    )