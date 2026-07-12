from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from models.user import User

from schemas.product import (
    ProductCreate,
    ProductResponse
)
from services.product import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "/",
    response_model=ProductResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("product", "create"))
    ]
)
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


@router.get(
    "/",
    response_model=list[ProductResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("product", "view"))
    ]
)
def list_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_products(
        db,
        current_user
    )


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("product", "view"))
    ]
)
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

@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("product", "update"))
    ]
)
def update(
    product_id: int,
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_product(
        db,
        product_id,
        data,
        current_user
    )
@router.delete(
    "/{product_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("product", "delete"))
    ]
)
def delete(
    product_id: int,
    db: Session = Depends(get_db)
):
    return delete_product(
        db,
        product_id
    )