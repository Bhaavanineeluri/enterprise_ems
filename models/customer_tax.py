from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class CustomerTax(Base):
    __tablename__ = "customer_taxes"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    gst_number = Column(String(100))
    pan_number = Column(String(50))

    is_verified = Column(Boolean, default=False)

    customer = relationship("Customer", back_populates="customer_taxes")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())