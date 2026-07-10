from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class CompanyPolicy(Base):
    __tablename__ = "company_policies"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    policy_name = Column(String(150))
    policy_type = Column(String(100))

    description = Column(Text)

    version = Column(String(20))

    is_active = Column(Boolean, default=True)

    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="company_policies")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())