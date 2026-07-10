from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class GeneralLedger(Base):
    __tablename__ = "general_ledger"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    account_code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    account_name = Column(
        String(150),
        nullable=False
    )

    account_type = Column(
        String(50),
        nullable=False
    )

    opening_balance = Column(
        Float,
        default=0
    )

    current_balance = Column(
        Float,
        default=0
    )

    description = Column(
        String(255)
    )

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    company = relationship("Company")

    

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )