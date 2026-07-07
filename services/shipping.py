from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.shipment import Shipment
from models.delivery import Delivery
from models.sales_order import SalesOrder


# =====================================================
# CREATE SHIPMENT
# =====================================================

def create_shipment(db: Session, data):

    # Check Sales Order
    sales_order = db.query(SalesOrder).filter(
        SalesOrder.id == data.sales_order_id
    ).first()

    if not sales_order:
        raise HTTPException(
            status_code=404,
            detail="Sales Order not found"
        )

    # Prevent duplicate Shipment Number
    existing = db.query(Shipment).filter(
        Shipment.shipment_number == data.shipment_number
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Shipment already exists"
        )

    shipment = Shipment(
        shipment_number=data.shipment_number,
        sales_order_id=data.sales_order_id,
        shipped_by=data.shipped_by,
        courier_name=data.courier_name,
        tracking_number=data.tracking_number,
        status="Shipped"
    )

    # Optional: Update Sales Order status
    sales_order.status = "Shipped"

    db.add(shipment)
    db.commit()
    db.refresh(shipment)

    return shipment


# =====================================================
# GET SHIPMENTS
# =====================================================

def get_shipments(db: Session):
    return db.query(Shipment).all()


def get_shipment(db: Session, shipment_id: int):

    shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )

    return shipment


# =====================================================
# CREATE DELIVERY
# =====================================================

def create_delivery(db: Session, data):

    shipment = db.query(Shipment).filter(
        Shipment.id == data.shipment_id
    ).first()

    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )

    delivery = Delivery(
        delivery_number=data.delivery_number,
        shipment_id=data.shipment_id,
        delivered_to=data.delivered_to,
        delivered_by=data.delivered_by,
        received_by=data.received_by,
        remarks=data.remarks,
        delivery_status="Delivered"
    )

    # Update Shipment status
    shipment.status = "Delivered"

    # Update Sales Order status
    sales_order = db.query(SalesOrder).filter(
        SalesOrder.id == shipment.sales_order_id
    ).first()

    if sales_order:
        sales_order.status = "Delivered"

    db.add(delivery)

    db.commit()
    db.refresh(delivery)

    return delivery


# =====================================================
# GET DELIVERIES
# =====================================================

def get_deliveries(db: Session):
    return db.query(Delivery).all()


def get_delivery(db: Session, delivery_id: int):

    delivery = db.query(Delivery).filter(
        Delivery.id == delivery_id
    ).first()

    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found"
        )

    return delivery