from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class CompanyLicense(Base):
    __tablename__ = "company_licenses"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    license_name = Column(String(150))
    license_number = Column(String(100))

    issue_date = Column(Date)
    expiry_date = Column(Date)

    issuing_authority = Column(String(150))

    is_active = Column(Boolean, default=True)

    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="company_licenses")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())