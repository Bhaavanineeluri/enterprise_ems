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


class GoodsReceipt(Base):

    __tablename__ = "goods_receipts"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    grn_number = Column(
        String(50),
        unique=True,
        nullable=False
    )


    purchase_order_id = Column(
        Integer,
        ForeignKey("purchase_orders.id"),
        nullable=False
    )


    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )


    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id")
    )


    received_quantity = Column(
        Integer,
        nullable=False
    )


    received_by = Column(
        Integer,
        ForeignKey("users.id")
    )


    remarks = Column(
        String(255)
    )


    purchase_order = relationship(
        "PurchaseOrder"
    )


    product = relationship(
        "Product"
    )


    vendor = relationship(
        "Vendor",
        back_populates="goods_receipts"
    )


    receiver = relationship(
        "User"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )