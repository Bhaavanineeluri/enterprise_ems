from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies.auth import get_current_user

from models.user import User

from schemas.product import (
    ProductCreate,
    ProductResponse
)

from services.product import (
    create_product,
    get_products,
    get_product,
    delete_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=ProductResponse)
def create(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_product(
        db,
        data,
        current_user
    )


@router.get("/", response_model=list[ProductResponse])
def list_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_products(
        db,
        current_user
    )


@router.get("/{product_id}", response_model=ProductResponse)
def get_one(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_product(
        db,
        product_id,
        current_user
    )
@router.delete("/{product_id}")
def delete(
    product_id: int,
    db: Session = Depends(get_db)
):

    return delete_product(
        db,
        product_id
    )