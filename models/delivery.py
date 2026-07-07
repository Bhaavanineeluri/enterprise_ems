from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)

    delivery_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    shipment_id = Column(
        Integer,
        ForeignKey("shipments.id"),
        nullable=False
    )

    delivered_to = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    delivered_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    delivery_status = Column(
        String(30),
        default="Delivered"
    )

    received_by = Column(String(100))

    remarks = Column(String(255))

    delivered_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )