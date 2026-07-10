from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    reference_no = Column(
        String(50),
        unique=True,
        nullable=False
    )

    description = Column(
        String(255)
    )

    entry_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    company = relationship("Company")

    user = relationship("User")

    
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )