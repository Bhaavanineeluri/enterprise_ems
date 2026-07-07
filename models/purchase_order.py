from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)

    po_number = Column(String(50), unique=True)

    purchase_request_id = Column(
        Integer,
        ForeignKey("purchase_requests.id")
    )

    status = Column(String(30), default="Created")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )