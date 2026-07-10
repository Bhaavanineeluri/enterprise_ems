from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_code = Column(
        String(50),
        unique=True,
        index=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    category = Column(String(100))

    brand = Column(String(100))

    price = Column(
        Float,
        nullable=False
    )

    cost_price = Column(Float)
    minimum_stock = Column(
    Integer,
    default=10,
    nullable=False
)

    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id")
    )

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )


    # ==========================
    # Parent Relationships
    # ==========================

    company = relationship(
        "Company"
    )

    vendor = relationship(
        "Vendor",
        back_populates="products"
    )


    inventory = relationship(
        "Inventory",
        back_populates="product",
        uselist=False
    )


    # ==========================
    # Product Child Relationships
    # ==========================
    # ==========================
# Product Child Tables
# ==========================

    product_images = relationship(
    "ProductImage",
    back_populates="product",
    cascade="all, delete-orphan"
    )


    product_attributes = relationship(
    "ProductAttribute",
    back_populates="product",
    cascade="all, delete-orphan"
    )


    product_price_histories = relationship(
    "ProductPriceHistory",
    back_populates="product",
    cascade="all, delete-orphan"
    )


    product_barcodes = relationship(
    "ProductBarcode",
    back_populates="product",
    cascade="all, delete-orphan"
    )


    product_suppliers = relationship(
    "ProductSupplier",
    back_populates="product",
    cascade="all, delete-orphan"
    )
