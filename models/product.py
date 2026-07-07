from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    product_code = Column(String(50), unique=True, index=True)
    name = Column(String(150), nullable=False)

    category = Column(String(100))
    brand = Column(String(100))

    price = Column(Float, nullable=False)
    cost_price = Column(Float)

    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())