from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class CustomerNote(Base):
    __tablename__ = "customer_notes"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    title = Column(String(150))
    note = Column(String(500))

    customer = relationship("Customer", back_populates="customer_notes")

    created_at = Column(DateTime(timezone=True), server_default=func.now())