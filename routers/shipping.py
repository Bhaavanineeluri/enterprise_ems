from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.shipping import (
    ShipmentCreate,
    DeliveryCreate
)

from services.shipping import (
    create_shipment,
    get_shipments,
    get_shipment,
    create_delivery,
    get_deliveries,
    get_delivery
)

router = APIRouter(
    prefix="/shipping",
    tags=["Shipping"]
)


# =====================================================
# SHIPMENT
# =====================================================

@router.post(
    "/shipments",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("shipping", "create"))
    ]
)
def create_new_shipment(
    data: ShipmentCreate,
    db: Session = Depends(get_db)
):
    return create_shipment(db, data)


@router.get(
    "/shipments",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("shipping", "view"))
    ]
)
def list_shipments(
    db: Session = Depends(get_db)
):
    return get_shipments(db)


@router.get(
    "/shipments/{shipment_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("shipping", "view"))
    ]
)
def get_single_shipment(
    shipment_id: int,
    db: Session = Depends(get_db)
):
    return get_shipment(db, shipment_id)


# =====================================================
# DELIVERY
# =====================================================

@router.post(
    "/deliveries",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("shipping", "create"))
    ]
)
def create_new_delivery(
    data: DeliveryCreate,
    db: Session = Depends(get_db)
):
    return create_delivery(db, data)


@router.get(
    "/deliveries",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("shipping", "view"))
    ]
)
def list_deliveries(
    db: Session = Depends(get_db)
):
    return get_deliveries(db)


@router.get(
    "/deliveries/{delivery_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("shipping", "view"))
    ]
)
def get_single_delivery(
    delivery_id: int,
    db: Session = Depends(get_db)
):
    return get_delivery(db, delivery_id)