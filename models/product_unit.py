from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from database import Base


class ProductUnit(Base):
    __tablename__ = "product_units"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(100),
        nullable=False
    )

    symbol = Column(
        String(20),
        nullable=False
    )

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )