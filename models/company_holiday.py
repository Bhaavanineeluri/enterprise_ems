from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class CompanyHoliday(Base):
    __tablename__ = "company_holidays"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    holiday_name = Column(String(150))
    holiday_date = Column(Date)

    holiday_type = Column(String(50))

    is_active = Column(Boolean, default=True)

    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="company_holidays")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())