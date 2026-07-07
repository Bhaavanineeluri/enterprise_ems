from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from schemas.vendor import VendorCreate



def create_vendor(
    db: Session,
    data: VendorCreate
):

    uow = UnitOfWork(db)


    existing = uow.vendors.first_by(
        db,
        vendor_code=data.vendor_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Vendor code already exists"
        )


    try:

        vendor = uow.vendors.model(
            **data.model_dump()
        )


        uow.vendors.create(
            db,
            vendor
        )


        uow.commit()

        uow.refresh(vendor)


        return vendor


    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Vendor creation failed: {str(e)}"
        )




def get_vendors(db: Session):

    uow = UnitOfWork(db)

    return uow.vendors.get_all(db)