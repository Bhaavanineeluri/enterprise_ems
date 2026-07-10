from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class StockSerial(Base):
    __tablename__ = "stock_serials"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))

    serial_number = Column(String(150), unique=True)

    is_sold = Column(Boolean, default=False)

    product = relationship("Product")

    created_at = Column(DateTime(timezone=True), server_default=func.now())