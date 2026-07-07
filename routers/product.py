from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.product import ProductCreate, ProductResponse
from services.product import create_product, get_products, get_product

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, data)


@router.get("/", response_model=list[ProductResponse])
def list_all(
    page: int =1,
    limit: int =10,
    db: Session = Depends(get_db)):
    
    return get_products(
        db,
        page,
        limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_one(product_id: int, db: Session = Depends(get_db)):
    return get_product(db, product_id)