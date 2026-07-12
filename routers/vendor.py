from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.vendor import (
    VendorCreate,
    VendorResponse,
    VendorEvaluation
)

from services.vendor import (
    create_vendor,
    get_vendors,
    get_vendor,
    update_vendor,
    delete_vendor,
    evaluate_vendor,
    purchase_history
)

router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)


@router.post(
    "/",
    response_model=VendorResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "create"))
    ]
)
def create(
    data: VendorCreate,
    db: Session = Depends(get_db)
):
    return create_vendor(db, data)


@router.get(
    "/",
    response_model=list[VendorResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "view"))
    ]
)
def list_all(
    db: Session = Depends(get_db)
):
    return get_vendors(db)


@router.get(
    "/{vendor_id}",
    response_model=VendorResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "view"))
    ]
)
def get_one(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    return get_vendor(db, vendor_id)


@router.put(
    "/{vendor_id}",
    response_model=VendorResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "update"))
    ]
)
def update(
    vendor_id: int,
    data: VendorCreate,
    db: Session = Depends(get_db)
):
    return update_vendor(db, vendor_id, data)


@router.put(
    "/{vendor_id}/evaluation",
    response_model=VendorResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "evaluate"))
    ]
)
def evaluate(
    vendor_id: int,
    data: VendorEvaluation,
    db: Session = Depends(get_db)
):
    return evaluate_vendor(
        db,
        vendor_id,
        data.rating,
        data.remarks
    )


@router.get(
    "/{vendor_id}/purchase-history",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "view"))
    ]
)
def history(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    return purchase_history(db, vendor_id)


@router.delete(
    "/{vendor_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("vendor", "delete"))
    ]
)
def delete(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    return delete_vendor(db, vendor_id)