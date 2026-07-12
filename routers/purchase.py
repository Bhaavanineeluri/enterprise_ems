from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.purchase import (
    PurchaseRequestCreate,
    PurchaseRequestResponse,
    PurchaseOrderCreate,
    PurchaseOrderResponse,
)

from services.purchase import (
    create_purchase_request,
    create_purchase_order,
    get_purchase_requests,
    get_purchase_orders,
)

router = APIRouter(
    prefix="/purchase",
    tags=["Procurement"]
)


@router.post(
    "/request",
    response_model=PurchaseRequestResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("purchase", "create"))
    ]
)
def create_request(
    data: PurchaseRequestCreate,
    db: Session = Depends(get_db)
):
    return create_purchase_request(db, data)


@router.get(
    "/request",
    response_model=list[PurchaseRequestResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("purchase", "view"))
    ]
)
def list_requests(
    db: Session = Depends(get_db)
):
    return get_purchase_requests(db)


@router.post(
    "/order",
    response_model=PurchaseOrderResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("purchase", "create"))
    ]
)
def create_order(
    data: PurchaseOrderCreate,
    db: Session = Depends(get_db)
):
    return create_purchase_order(db, data)


@router.get(
    "/order",
    response_model=list[PurchaseOrderResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("purchase", "view"))
    ]
)
def list_orders(
    db: Session = Depends(get_db)
):
    return get_purchase_orders(db)