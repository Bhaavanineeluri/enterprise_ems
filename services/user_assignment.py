from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork



def assign_user(
    db:Session,
    user_id:int,
    company_id:int=None,
    branch_id:int=None,
    department_id:int=None,
    team_id:int=None
):

    uow = UnitOfWork(db)



    user = uow.users.get(
        db,
        user_id
    )


    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



    try:


        if company_id:

            if not uow.companies.get(
                db,
                company_id
            ):

                raise HTTPException(
                    status_code=404,
                    detail="Company not found"
                )


            user.company_id = company_id




        if branch_id:

            if not uow.branches.get(
                db,
                branch_id
            ):

                raise HTTPException(
                    status_code=404,
                    detail="Branch not found"
                )


            user.branch_id = branch_id




        if department_id:

            if not uow.departments.get(
                db,
                department_id
            ):

                raise HTTPException(
                    status_code=404,
                    detail="Department not found"
                )


            user.department_id = department_id




        if team_id:

            if not uow.teams.get(
                db,
                team_id
            ):

                raise HTTPException(
                    status_code=404,
                    detail="Team not found"
                )


            user.team_id = team_id




        uow.commit()

        uow.refresh(user)


        return user



    except Exception:

        uow.rollback()

        raise