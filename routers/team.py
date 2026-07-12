from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.team import TeamCreate, TeamResponse
from services.team import (
    create_team,
    get_all_teams,
    get_team
)

router = APIRouter(
    prefix="/teams",
    tags=["Team"]
)


@router.post(
    "/",
    response_model=TeamResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("team", "create"))
    ]
)
def create(
    data: TeamCreate,
    db: Session = Depends(get_db)
):
    return create_team(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[TeamResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("team", "view"))
    ]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_teams(db)


@router.get(
    "/{team_id}",
    response_model=TeamResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("team", "view"))
    ]
)
def get_one(
    team_id: int,
    db: Session = Depends(get_db)
):
    return get_team(
        db,
        team_id
    )