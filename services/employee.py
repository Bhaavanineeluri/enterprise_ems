from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from schemas.employee import EmployeeCreate



def create_employee(
    db:Session,
    data:EmployeeCreate
):

    uow = UnitOfWork(db)


    user = uow.users.get(
        db,
        data.user_id
    )


    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



    existing = uow.employees.first_by(
        db,
        user_id=data.user_id
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Employee profile already exists"
        )


    try:

        employee = uow.employees.model(
            **data.model_dump()
        )


        uow.employees.create(
            db,
            employee
        )


        uow.commit()

        uow.refresh(employee)


        return employee


    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Employee creation failed: {str(e)}"
        )




def get_employees(db:Session):

    uow = UnitOfWork(db)

    return uow.employees.get_all(db)