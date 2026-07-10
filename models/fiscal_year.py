from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class FiscalYear(Base):
    __tablename__ = "fiscal_years"

    id = Column(Integer, primary_key=True)

    fiscal_name = Column(String(100))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    created_at = Column(DateTime(timezone=True), server_default=func.now())