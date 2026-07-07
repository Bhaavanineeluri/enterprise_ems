from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class PurchaseRequest(Base):
    __tablename__ = "purchase_requests"

    id = Column(Integer, primary_key=True, index=True)

    request_no = Column(String(50), unique=True, nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"))
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    quantity = Column(Integer, nullable=False)

    status = Column(String(30), default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )