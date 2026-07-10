from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from database import Base


class ProductBrand(Base):
    __tablename__ = "product_brands"

    id = Column(Integer, primary_key=True)

    name = Column(String(150), nullable=False)

    code = Column(String(50), unique=True)

    manufacturer = Column(String(150))

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )