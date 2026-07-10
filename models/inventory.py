from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        unique=True
    )

    quantity = Column(
        Integer,
        default=0
    )

    # ==========================
    # Existing Relationships
    # ==========================

    product = relationship(
        "Product",
        back_populates="inventory"
    )

    # ==========================
    # Inventory Module
    # ==========================


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )