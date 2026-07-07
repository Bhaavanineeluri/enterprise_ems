from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.team import TeamCreate

from core.unit_of_work.uow import UnitOfWork



def create_team(
    db:Session,
    data:TeamCreate
):

    uow = UnitOfWork(db)



    department = uow.departments.get(
        db,
        data.department_id
    )


    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )



    existing = uow.teams.first_by(
        db,
        team_code=data.team_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Team code already exists"
        )



    try:

        team = uow.teams.model(
            **data.model_dump()
        )


        uow.teams.create(
            db,
            team
        )


        uow.commit()

        uow.refresh(team)


        return team



    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Team creation failed: {str(e)}"
        )




def get_all_teams(db:Session):

    uow = UnitOfWork(db)

    return uow.teams.get_all(db)




def get_team(
    db:Session,
    team_id:int
):

    uow = UnitOfWork(db)

    team = uow.teams.get(
        db,
        team_id
    )


    if not team:

        raise HTTPException(
            status_code=404,
            detail="Team not found"
        )


    return team