from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    customer_code = Column(
        String(50),
        unique=True,
        index=True,
        nullable=True
    )

    company_name = Column(
        String(150),
        nullable=True
    )

    address = Column(
        String(255),
        nullable=True
    )

    city = Column(
        String(100),
        nullable=True
    )

    state = Column(
        String(100),
        nullable=True
    )

    country = Column(
        String(100),
        nullable=True
    )


    # ==========================
    # Existing Relationships
    # ==========================

    user = relationship(
        "User",
        back_populates="customer"
    )

    invoices = relationship(
        "Invoice",
        back_populates="customer"
    )


    # ==========================
    # Customer Module Relationships
    # ==========================

    customer_addresses = relationship(
        "CustomerAddress",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_attachments = relationship(
        "CustomerAttachment",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_bank_accounts = relationship(
        "CustomerBankAccount",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_contacts = relationship(
        "CustomerContact",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_credit_limits = relationship(
        "CustomerCreditLimit",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_documents = relationship(
        "CustomerDocument",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_feedbacks = relationship(
        "CustomerFeedback",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_interactions = relationship(
        "CustomerInteraction",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_notes = relationship(
        "CustomerNote",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_preferences = relationship(
        "CustomerPreference",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    customer_taxes = relationship(
        "CustomerTax",
        back_populates="customer",
        cascade="all, delete-orphan"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )