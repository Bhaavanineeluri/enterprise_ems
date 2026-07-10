from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String(150), nullable=False, unique=True)
    company_code = Column(String(50), nullable=False, unique=True)

    email = Column(String(150))
    phone = Column(String(20))
    website = Column(String(150))
    address = Column(String(255))

    is_active = Column(Boolean, default=True)

    # ==========================
    # Existing Relationships
    # ==========================

    users = relationship(
        "User",
        back_populates="company"
    )

    branches = relationship(
        "Branch",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    # ==========================
    # Company Module
    # ==========================

    company_addresses = relationship(
        "CompanyAddress",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_contacts = relationship(
        "CompanyContact",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_bank_accounts = relationship(
        "CompanyBankAccount",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_taxes = relationship(
        "CompanyTax",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_licenses = relationship(
        "CompanyLicense",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_policies = relationship(
        "CompanyPolicy",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_holidays = relationship(
        "CompanyHoliday",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    company_settings = relationship(
        "CompanySetting",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    fiscal_years = relationship(
        "CompanyFiscalYear",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    working_hours = relationship(
        "CompanyWorkingHours",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    # Optional (only if you created these models)
