from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.team import Team
from models.department import Department
from schemas.team import TeamCreate


def create_team(db: Session, data: TeamCreate):

    department = db.query(Department).filter(
        Department.id == data.department_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    existing = db.query(Team).filter(
        Team.team_code == data.team_code
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Team code already exists"
        )

    team = Team(
        team_name=data.team_name,
        team_code=data.team_code,
        description=data.description,
        department_id=data.department_id
    )

    db.add(team)
    db.commit()
    db.refresh(team)

    return team


def get_all_teams(db: Session):
    return db.query(Team).all()


def get_team(db: Session, team_id: int):

    team = db.query(Team).filter(
        Team.id == team_id
    ).first()

    if not team:
        raise HTTPException(
            status_code=404,
            detail="Team not found"
        )

    return team