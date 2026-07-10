from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from schemas.product import ProductCreate


# ---------------------------------
# CREATE PRODUCT
# ---------------------------------
def create_product(
    db: Session,
    data: ProductCreate,
    current_user
):

    uow = UnitOfWork(db)

    existing = uow.products.first_by(
        db,
        product_code=data.product_code,
        company_id=current_user.company_id
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Product already exists"
        )

    try:

        payload = data.model_dump()

        # Automatically assign logged-in user's company
        payload["company_id"] = current_user.company_id

        product = uow.products.model(
            **payload
        )

        uow.products.create(
            db,
            product
        )

        uow.commit()
        uow.refresh(product)

        return product

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Product creation failed: {str(e)}"
        )


# ---------------------------------
# GET ALL PRODUCTS
# ---------------------------------
def get_products(
    db: Session,
    current_user
):

    uow = UnitOfWork(db)

    return uow.products.all_by(
        db,
        company_id=current_user.company_id
    )


# ---------------------------------
# GET SINGLE PRODUCT
# ---------------------------------
def get_product(
    db: Session,
    product_id: int,
    current_user
):

    uow = UnitOfWork(db)

    product = uow.products.first_by(
        db,
        id=product_id,
        company_id=current_user.company_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product
# =====================================================
# DELETE PRODUCT
# =====================================================

def delete_product(
    db: Session,
    product_id: int
):

    uow = UnitOfWork(db)

    product = uow.products.get(
        db,
        product_id
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    try:

        uow.products.delete(
            db,
            product
        )

        uow.commit()

        return {
            "success": True,
            "message": "Product deleted successfully"
        }

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )