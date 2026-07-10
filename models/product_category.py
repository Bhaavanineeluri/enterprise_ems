from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True)

    name = Column(String(150), nullable=False)
    code = Column(String(50), unique=True)
    description = Column(String(255))

    is_active = Column(Boolean, default=True)


    product_subcategories = relationship(
        "ProductSubCategory",
        back_populates="product_category",
        cascade="all, delete-orphan"
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