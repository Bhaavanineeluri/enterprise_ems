from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Date,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class AccountsPayable(Base):

    __tablename__ = "accounts_payable"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id"),
        nullable=False
    )


    bill_number = Column(
        String(100),
        nullable=False,
        unique=True
    )


    amount = Column(
        Float,
        nullable=False
    )


    paid_amount = Column(
        Float,
        default=0
    )


    due_date = Column(
        Date
    )


    status = Column(
        String(50),
        default="PENDING"
    )


    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )


    vendor = relationship(
        "Vendor"
    )


    company = relationship(
        "Company"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )