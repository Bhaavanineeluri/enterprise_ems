from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class AccountingPeriod(Base):
    __tablename__ = "accounting_periods"

    id = Column(Integer, primary_key=True)

    fiscal_year_id = Column(Integer, ForeignKey("fiscal_years.id"))

    period_name = Column(String(100))

    start_date = Column(DateTime)
    end_date = Column(DateTime)

    fiscal_year = relationship("FiscalYear")

    created_at = Column(DateTime(timezone=True), server_default=func.now())