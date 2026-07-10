from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.customer import (
    create_customer,
    get_all_customers,
    get_customer,
    delete_customer
)
from database import get_db
from schemas.customer import CustomerCreate, CustomerResponse
from services.customer import create_customer, get_customers, get_customer
from schemas.customer import CustomerUpdate, CustomerResponse
from services.customer import update_customer
router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse)
def create(data: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, data)


@router.get("/", response_model=list[CustomerResponse])
def list_all(db: Session = Depends(get_db)):
    return get_customers(db)


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def update_customer_by_id(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db)
):
    return update_customer(
        customer_id,
        customer,
        db
    )
@router.get("/")
def read_all_customers(db: Session = Depends(get_db)):
    return get_all_customers(db)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_one(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(db, customer_id)

@router.delete("/{customer_id}")
def delete(
    customer_id: int,
    db: Session = Depends(get_db)
):

    return delete_customer(
        db,
        customer_id
    )