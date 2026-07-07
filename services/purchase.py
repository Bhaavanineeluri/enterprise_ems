from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork



# =====================================================
# CREATE PURCHASE REQUEST
# =====================================================

def create_purchase_request(
    db: Session,
    data
):

    uow = UnitOfWork(db)


    existing = uow.purchase_requests.first_by(
        db,
        request_no=data.request_no
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Purchase Request already exists"
        )


    try:

        request = uow.purchase_requests.model(
            **data.model_dump()
        )


        uow.purchase_requests.create(
            db,
            request
        )


        uow.commit()

        uow.refresh(request)


        return request



    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Purchase request failed: {str(e)}"
        )




# =====================================================
# GET PURCHASE REQUESTS
# =====================================================

def get_purchase_requests(
    db:Session
):

    uow = UnitOfWork(db)

    return uow.purchase_requests.get_all(db)




# =====================================================
# CREATE PURCHASE ORDER
# =====================================================

def create_purchase_order(
    db:Session,
    data
):

    uow = UnitOfWork(db)



    request = uow.purchase_requests.get(
        db,
        data.purchase_request_id
    )


    if not request:

        raise HTTPException(
            status_code=404,
            detail="Purchase Request not found"
        )



    try:

        order = uow.purchase_orders.model(

            po_number=data.po_number,

            purchase_request_id=data.purchase_request_id,

            status="Approved"

        )


        request.status = "Approved"


        uow.purchase_orders.create(
            db,
            order
        )


        uow.commit()

        uow.refresh(order)


        return order



    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Purchase order failed: {str(e)}"
        )





def get_purchase_orders(
    db:Session
):

    uow = UnitOfWork(db)

    return uow.purchase_orders.get_all(db)