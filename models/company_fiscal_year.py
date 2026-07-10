from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from database import Base


class CompanyFiscalYear(Base):
    __tablename__ = "company_fiscal_years"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    start_date = Column(Date)
    end_date = Column(Date)

    is_current = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="fiscal_years")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())