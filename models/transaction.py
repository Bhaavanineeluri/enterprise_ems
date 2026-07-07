from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

from sqlalchemy.orm import relationship
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    transaction_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    payment_id = Column(
        Integer,
        ForeignKey("payments.id"),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    transaction_type = Column(
        String(30),
        nullable=False
    )  # Credit / Debit

    reference = Column(
        String(100)
    )

    status = Column(
        String(30),
        default="Success"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    payment = relationship(
    "Payment",
    back_populates="transactions"
    )