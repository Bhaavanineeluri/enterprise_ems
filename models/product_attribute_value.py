from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductAttributeValue(Base):
    __tablename__ = "product_attribute_values"

    id = Column(
        Integer,
        primary_key=True
    )

    attribute_id = Column(
        Integer,
        ForeignKey("product_attributes.id"),
        nullable=False
    )

    value = Column(
        String(150),
        nullable=False
    )


    attribute = relationship(
        "ProductAttribute",
        back_populates="product_attribute_values"
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