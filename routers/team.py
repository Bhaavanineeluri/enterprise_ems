from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.team import TeamCreate, TeamResponse
from services.team import create_team, get_all_teams, get_team

router = APIRouter(prefix="/teams", tags=["Team"])


@router.post("/", response_model=TeamResponse)
def create(data: TeamCreate, db: Session = Depends(get_db)):
    return create_team(db, data)


@router.get("/", response_model=list[TeamResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_teams(db)


@router.get("/{team_id}", response_model=TeamResponse)
def get_one(team_id: int, db: Session = Depends(get_db)):
    return get_team(db, team_id)