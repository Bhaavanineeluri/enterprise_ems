from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class Ledger(Base):
    __tablename__ = "ledgers"

    id = Column(Integer, primary_key=True, index=True)

    ledger_name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    account_type = Column(
        String(50),
        nullable=False
    )  # Asset, Liability, Income, Expense, Equity

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

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )