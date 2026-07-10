from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True)

    currency_id = Column(Integer, ForeignKey("currencies.id"))

    exchange_rate = Column(Float, nullable=False)

    effective_date = Column(DateTime)

    currency = relationship("Currency")

    created_at = Column(DateTime(timezone=True), server_default=func.now())