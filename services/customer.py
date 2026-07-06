from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.customer import Customer


def create_customer(db: Session, data):

    existing = db.query(Customer).filter(
        Customer.customer_code == data.customer_code
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Customer exists")

    customer = Customer(**data.dict())

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Not found")

    return customer