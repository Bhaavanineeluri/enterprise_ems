from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Invoice(Base):

    __tablename__ = "invoices"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    invoice_number = Column(
        String(50),
        unique=True,
        nullable=False
    )


    sales_order_id = Column(
        Integer,
        ForeignKey("sales_orders.id"),
        nullable=False
    )


    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )


    total_amount = Column(
        Float,
        nullable=False
    )


    payment_status = Column(
        String(30),
        default="Pending"
    )


    invoice_status = Column(
        String(30),
        default="Generated"
    )


    customer = relationship(
        "Customer",
        back_populates="invoices"
    )


    payments = relationship(
        "Payment",
        back_populates="invoice"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )