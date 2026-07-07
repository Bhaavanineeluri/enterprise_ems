from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from schemas.customer import CustomerCreate



def create_customer(
    db:Session,
    data:CustomerCreate
):

    uow = UnitOfWork(db)


    existing = uow.customers.first_by(
        db,
        customer_code=data.customer_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Customer already exists"
        )



    try:

        customer = uow.customers.model(
            **data.model_dump()
        )


        uow.customers.create(
            db,
            customer
        )


        uow.commit()

        uow.refresh(customer)


        return customer


    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Customer creation failed: {str(e)}"
        )




def get_customers(db:Session):

    uow = UnitOfWork(db)

    return uow.customers.get_all(db)




def get_customer(
    db:Session,
    customer_id:int
):

    uow = UnitOfWork(db)


    customer = uow.customers.get(
        db,
        customer_id
    )


    if not customer:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )


    return customer