from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork



def create_goods_receipt(
    db:Session,
    data
):

    uow = UnitOfWork(db)



    purchase_order = uow.purchase_orders.get(
        db,
        data.purchase_order_id
    )


    if not purchase_order:

        raise HTTPException(
            status_code=404,
            detail="Purchase Order not found"
        )



    product = uow.products.get(
        db,
        data.product_id
    )


    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )



    existing = uow.goods_receipts.first_by(
        db,
        grn_number=data.grn_number
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="GRN already exists"
        )



    try:


        receipt = uow.goods_receipts.model(

            grn_number=data.grn_number,

            purchase_order_id=data.purchase_order_id,

            product_id=data.product_id,

            received_quantity=data.received_quantity,

            received_by=data.received_by,

            remarks=data.remarks
        )


        uow.goods_receipts.create(
            db,
            receipt
        )



        inventory = uow.inventory.first_by(
            db,
            product_id=data.product_id
        )



        if inventory:

            inventory.quantity += data.received_quantity


        else:

            inventory = uow.inventory.model(

                product_id=data.product_id,

                quantity=data.received_quantity

            )


            uow.inventory.create(
                db,
                inventory
            )



        purchase_order.status = "Received"



        uow.commit()

        uow.refresh(receipt)


        return receipt



    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Goods receipt failed: {str(e)}"
        )





def get_goods_receipts(
    db:Session
):

    uow = UnitOfWork(db)

    return uow.goods_receipts.get_all(db)