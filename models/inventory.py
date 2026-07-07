from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"), unique=True)

    quantity = Column(Integer, default=0)

    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())