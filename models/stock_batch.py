from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class StockBatch(Base):
    __tablename__ = "stock_batches"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))

    batch_number = Column(String(100), unique=True)

    manufacture_date = Column(DateTime)
    expiry_date = Column(DateTime)

    quantity = Column(Integer)

    product = relationship("Product")

    created_at = Column(DateTime(timezone=True), server_default=func.now())