from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductAttribute(Base):
    __tablename__ = "product_attributes"

    id = Column(
        Integer,
        primary_key=True
    )

    attribute_name = Column(
        String(100),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )


    product = relationship(
        "Product",
        back_populates="product_attributes"
    )


    product_attribute_values = relationship(
        "ProductAttributeValue",
        back_populates="attribute",
        cascade="all, delete-orphan"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )