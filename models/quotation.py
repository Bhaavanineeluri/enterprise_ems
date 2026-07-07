from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class Quotation(Base):
    __tablename__ = "quotations"

    id = Column(Integer, primary_key=True, index=True)

    quotation_number = Column(String(50), unique=True, nullable=False)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(Integer, nullable=False)

    unit_price = Column(Float, nullable=False)

    total_amount = Column(Float, nullable=False)

    status = Column(String(30), default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )