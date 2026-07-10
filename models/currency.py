from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)

    currency_name = Column(String(100), nullable=False)
    currency_code = Column(String(10), unique=True, nullable=False)
    currency_symbol = Column(String(10))

    is_base_currency = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())