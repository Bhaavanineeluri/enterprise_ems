from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductSubCategory(Base):
    __tablename__ = "product_subcategories"

    id = Column(Integer, primary_key=True)

    category_id = Column(
        Integer,
        ForeignKey("product_categories.id"),
        nullable=False
    )

    name = Column(String(150))
    code = Column(String(50))
    description = Column(String(255))

    is_active = Column(Boolean, default=True)


    product_category = relationship(
        "ProductCategory",
        back_populates="product_subcategories"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )