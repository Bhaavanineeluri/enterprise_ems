from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class StockAdjustment(Base):

    __tablename__ = "stock_adjustments"

    id = Column(
        Integer,
        primary_key=True
    )

    inventory_id = Column(
        Integer,
        ForeignKey("inventory.id"),
        nullable=False
    )

    adjustment_type = Column(
        String(10),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    reason = Column(
        String(255)
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    inventory = relationship("Inventory")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )