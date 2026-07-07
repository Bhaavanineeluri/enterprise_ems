from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    payment_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    invoice_id = Column(
        Integer,
        ForeignKey("invoices.id"),
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    payment_method = Column(
        String(50),
        nullable=False
    )

    payment_status = Column(
        String(30),
        default="Paid"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    invoice = relationship(
    "Invoice",
    back_populates="payments")


    transactions = relationship(
    "Transaction",
    back_populates="payment"
    )