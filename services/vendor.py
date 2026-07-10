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
def get_vendor(
    db: Session,
    vendor_id: int
):

    uow = UnitOfWork(db)

    vendor = uow.vendors.get(
        db,
        vendor_id
    )

    if not vendor:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return vendor
def update_vendor(
    db: Session,
    vendor_id: int,
    data: VendorCreate
):

    uow = UnitOfWork(db)

    vendor = uow.vendors.get(
        db,
        vendor_id
    )

    if not vendor:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    for key, value in data.model_dump().items():

        setattr(vendor, key, value)

    uow.commit()

    uow.refresh(vendor)

    return vendor
def delete_vendor(
    db: Session,
    vendor_id: int
):

    uow = UnitOfWork(db)

    vendor = uow.vendors.get(
        db,
        vendor_id
    )

    if not vendor:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    db.delete(vendor)

    uow.commit()

    return {
        "message": "Vendor deleted successfully"
    }
def evaluate_vendor(
    db: Session,
    vendor_id: int,
    rating: int,
    remarks: str
):

    uow = UnitOfWork(db)

    vendor = uow.vendors.get(
        db,
        vendor_id
    )

    if not vendor:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    vendor.rating = rating
    vendor.remarks = remarks

    uow.commit()

    uow.refresh(vendor)

    return vendor
def purchase_history(
    db: Session,
    vendor_id: int
):

    uow = UnitOfWork(db)

    vendor = uow.vendors.get(
        db,
        vendor_id
    )

    if not vendor:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return {
        "vendor_id": vendor.id,
        "vendor_name": vendor.name,
        "purchase_history": []
    }
# =====================================================
# DELETE VENDOR
# =====================================================

def delete_vendor(
    db: Session,
    vendor_id: int
):

    uow = UnitOfWork(db)

    vendor = uow.vendors.get(
        db,
        vendor_id
    )

    if not vendor:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    try:

        uow.vendors.delete(
            db,
            vendor
        )

        uow.commit()

        return {
            "success": True,
            "message": "Vendor deleted successfully"
        }

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )