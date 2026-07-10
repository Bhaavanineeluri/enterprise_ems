from sqlalchemy import Column, Integer, String, Time, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class CompanyWorkingHours(Base):
    __tablename__ = "company_working_hours"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    weekday = Column(String(20))

    start_time = Column(Time)
    end_time = Column(Time)

    break_start = Column(Time)
    break_end = Column(Time)

    is_working_day = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)

    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="working_hours")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())