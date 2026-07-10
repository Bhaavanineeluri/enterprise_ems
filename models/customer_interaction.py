from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class CustomerInteraction(Base):
    __tablename__ = "customer_interactions"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    interaction_type = Column(String(100))

    notes = Column(Text)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    customer = relationship(
    "Customer",
    back_populates="customer_interactions"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())