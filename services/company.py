from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.company import CompanyCreate

from core.unit_of_work.uow import UnitOfWork



def create_company(
    db: Session,
    data: CompanyCreate
):

    uow = UnitOfWork(db)


    existing = uow.companies.first_by(
        db,
        company_code=data.company_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Company code already exists"
        )


    try:

        company = uow.companies.model(
            **data.model_dump()
        )


        uow.companies.create(
            db,
            company
        )


        uow.commit()

        uow.refresh(company)


        return company


    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Company creation failed: {str(e)}"
        )




def get_all_companies(
    db: Session
):

    uow = UnitOfWork(db)

    return uow.companies.get_all(db)




def get_company(
    db: Session,
    company_id:int
):

    uow = UnitOfWork(db)

    company = uow.companies.get(
        db,
        company_id
    )


    if not company:

        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )


    return company