from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from schemas.customer import CustomerCreate

from models.customer import Customer
from schemas.customer import CustomerUpdate


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




def get_all_customers(db: Session):
    customers = db.query(Customer).all()

    if not customers:
        raise HTTPException(
            status_code=404,
            detail="No customers found."
        )

    return customers


def update_customer(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session
):
    db_customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    update_data = customer.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)

    return db_customer
# =====================================================
# DELETE CUSTOMER
# =====================================================

def delete_customer(
    db: Session,
    customer_id: int
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

    try:

        uow.customers.delete(
            db,
            customer
        )

        uow.commit()

        return {
            "success": True,
            "message": "Customer deleted successfully"
        }

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )