from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class CustomerBankAccount(Base):
    __tablename__ = "customer_bank_accounts"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    bank_name = Column(String(150))
    account_number = Column(String(50))
    ifsc_code = Column(String(20))
    branch_name = Column(String(150))

    is_primary = Column(Boolean, default=False)

    customer = relationship("Customer", back_populates="customer_bank_accounts")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())