from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.department import DepartmentCreate

from core.unit_of_work.uow import UnitOfWork



def create_department(
    db:Session,
    data:DepartmentCreate
):

    uow = UnitOfWork(db)



    branch = uow.branches.get(
        db,
        data.branch_id
    )


    if not branch:

        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )



    existing = uow.departments.first_by(
        db,
        department_code=data.department_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Department code already exists"
        )



    try:

        department = uow.departments.model(
            **data.model_dump()
        )


        uow.departments.create(
            db,
            department
        )


        uow.commit()

        uow.refresh(department)


        return department



    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Department creation failed: {str(e)}"
        )




def get_all_departments(db:Session):

    uow = UnitOfWork(db)

    return uow.departments.get_all(db)




def get_department(
    db:Session,
    department_id:int
):

    uow = UnitOfWork(db)

    department = uow.departments.get(
        db,
        department_id
    )


    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )


    return department