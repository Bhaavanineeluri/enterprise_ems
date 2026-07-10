from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductBarcode(Base):
    __tablename__ = "product_barcodes"

    id = Column(Integer, primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    barcode = Column(
        String(150),
        unique=True
    )

    product = relationship(
        "Product",
        back_populates="product_barcodes"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )