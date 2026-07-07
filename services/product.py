from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from schemas.product import ProductCreate



def create_product(
    db: Session,
    data: ProductCreate
):

    uow = UnitOfWork(db)


    existing = uow.products.first_by(
        db,
        product_code=data.product_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Product already exists"
        )


    try:

        product = uow.products.model(
            **data.model_dump()
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




def get_products(
    db: Session,
    page: int = 1,
    limit: int = 10
):

    uow = UnitOfWork(db)

    return uow.products.paginate_all(
        db,
        page,
        limit
    )




def get_product(
    db:Session,
    product_id:int
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


    return product