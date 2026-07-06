from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.customer import CustomerCreate, CustomerResponse
from services.customer_service import create_customer, get_customers, get_customer

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse)
def create(data: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, data)


@router.get("/", response_model=list[CustomerResponse])
def list_all(db: Session = Depends(get_db)):
    return get_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_one(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(db, customer_id)