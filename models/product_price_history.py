from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductPriceHistory(Base):
    __tablename__ = "product_price_history"

    id = Column(Integer, primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    old_price = Column(Float)
    new_price = Column(Float)

    product = relationship(
        "Product",
        back_populates="product_price_histories"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )