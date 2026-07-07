from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)

    journal_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    transaction_id = Column(
        Integer,
        ForeignKey("transactions.id"),
        nullable=False
    )

    account_name = Column(
        String(100),
        nullable=False
    )

    debit = Column(
        Float,
        default=0
    )

    credit = Column(
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