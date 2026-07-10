from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class StockTransferItem(Base):
    __tablename__ = "stock_transfer_items"

    id = Column(Integer, primary_key=True)

    transfer_id = Column(Integer, ForeignKey("stock_transfers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer)

    transfer = relationship(
        "StockTransfer",
        back_populates="items"
    )

    product = relationship("Product")