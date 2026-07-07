from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork



def add_or_update_inventory(
    db: Session,
    data
):

    uow = UnitOfWork(db)



    product = uow.products.get(
        db,
        data.product_id
    )


    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )



    inventory = uow.inventory.first_by(
        db,
        product_id=data.product_id
    )



    if inventory:

        inventory.quantity = data.quantity


    else:

        inventory = uow.inventory.model(

            product_id=data.product_id,

            quantity=data.quantity
        )


        uow.inventory.create(
            db,
            inventory
        )



    try:

        uow.commit()

        uow.refresh(inventory)

        return inventory


    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Inventory update failed: {str(e)}"
        )




def get_inventory(db:Session):

    uow = UnitOfWork(db)

    return uow.inventory.get_all(db)