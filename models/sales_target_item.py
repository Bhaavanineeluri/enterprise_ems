from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class SalesTargetItem(Base):
    __tablename__ = "sales_target_items"

    id = Column(Integer, primary_key=True)

    sales_target_id = Column(Integer, ForeignKey("sales_targets.id"))

    product_id = Column(Integer, ForeignKey("products.id"))

    target_quantity = Column(Float)

    target = relationship(
        "SalesTarget",
        back_populates="items"
    )