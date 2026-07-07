from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)

    shipment_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    sales_order_id = Column(
        Integer,
        ForeignKey("sales_orders.id"),
        nullable=False
    )

    shipped_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    courier_name = Column(String(100))

    tracking_number = Column(
        String(100),
        unique=True
    )

    status = Column(
        String(30),
        default="Shipped"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )