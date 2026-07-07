from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class GoodsReceipt(Base):
    __tablename__ = "goods_receipts"

    id = Column(Integer, primary_key=True, index=True)

    grn_number = Column(String(50), unique=True, nullable=False)

    purchase_order_id = Column(
        Integer,
        ForeignKey("purchase_orders.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    received_quantity = Column(Integer, nullable=False)

    received_by = Column(Integer, ForeignKey("users.id"))

    remarks = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )