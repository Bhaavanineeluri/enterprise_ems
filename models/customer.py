from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    customer_code = Column(String(50), unique=True, index=True)
    company_name = Column(String(150))

    address = Column(String(255))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))

    created_at = Column(DateTime(timezone=True), server_default=func.now())