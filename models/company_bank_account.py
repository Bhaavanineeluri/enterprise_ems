from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class CompanyBankAccount(Base):
    __tablename__ = "company_bank_accounts"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    bank_name = Column(String(150))
    branch_name = Column(String(150))
    account_name = Column(String(150))
    account_number = Column(String(50))
    ifsc_code = Column(String(20))
    swift_code = Column(String(20))

    is_default = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    company = relationship("Company", back_populates="company_bank_accounts")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())