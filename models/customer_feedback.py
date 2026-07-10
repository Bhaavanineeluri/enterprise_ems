from sqlalchemy import Column, Integer, Text, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class CustomerFeedback(Base):
    __tablename__ = "customer_feedback"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    rating = Column(Float)

    feedback = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    customer = relationship(
    "Customer",
    back_populates="customer_feedbacks"
    )