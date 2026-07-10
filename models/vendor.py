from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Boolean,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    vendor_code = Column(
        String(50),
        unique=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    email = Column(
        String(150)
    )

    phone = Column(
        String(20)
    )

    contract_number = Column(
        String(100),
        nullable=True
    )

    contract_start_date = Column(
        Date,
        nullable=True
    )

    contract_end_date = Column(
        Date,
        nullable=True
    )

    rating = Column(
        Integer,
        default=0
    )

    remarks = Column(
        String(255),
        nullable=True
    )

    is_compliant = Column(
        Boolean,
        default=True
    )


    # ==========================
    # Main Module Relationships
    # ==========================

    products = relationship(
        "Product",
        back_populates="vendor"
    )


    purchase_requests = relationship(
        "PurchaseRequest",
        back_populates="vendor"
    )


    purchase_orders = relationship(
        "PurchaseOrder",
        back_populates="vendor"
    )


    goods_receipts = relationship(
        "GoodsReceipt",
        back_populates="vendor"
    )


    # Product Supplier Mapping
    product_suppliers = relationship(
        "ProductSupplier",
        back_populates="vendor",
        cascade="all, delete-orphan"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )