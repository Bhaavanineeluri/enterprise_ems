from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class CustomerAttachment(Base):
    __tablename__ = "customer_attachments"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    file_name = Column(String(255))
    file_path = Column(String(255))
    file_type = Column(String(100))

    customer = relationship("Customer", back_populates="customer_attachments")

    created_at = Column(DateTime(timezone=True), server_default=func.now())