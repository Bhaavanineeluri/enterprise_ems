from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class PurchaseOrder(Base):

    __tablename__ = "purchase_orders"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    po_number = Column(
        String(50),
        unique=True
    )


    purchase_request_id = Column(
        Integer,
        ForeignKey("purchase_requests.id")
    )


    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id")
    )


    status = Column(
        String(30),
        default="Created"
    )


    purchase_request = relationship(
        "PurchaseRequest"
    )


    vendor = relationship(
        "Vendor",
        back_populates="purchase_orders"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )