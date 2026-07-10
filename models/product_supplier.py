from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductSupplier(Base):

    __tablename__ = "product_suppliers"

    id = Column(
        Integer,
        primary_key=True
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id"),
        nullable=False
    )


    product = relationship(
        "Product",
        back_populates="product_suppliers"
    )


    vendor = relationship(
        "Vendor",
        back_populates="product_suppliers"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )