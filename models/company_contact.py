from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class CompanyContact(Base):
    __tablename__ = "company_contacts"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    contact_person = Column(String(150))
    designation = Column(String(100))

    email = Column(String(150))
    phone = Column(String(20))
    mobile = Column(String(20))

    is_primary = Column(Boolean, default=False)

    remarks = Column(String(255))
    is_active = Column(Boolean, default=True)

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="company_contacts")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())