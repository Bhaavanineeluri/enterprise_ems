from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Numeric,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Opportunity(Base):

    __tablename__ = "opportunities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    title = Column(
        String(150),
        nullable=False
    )

    stage = Column(
        String(50),
        default="Prospecting"
    )
    # Prospecting, Proposal, Negotiation, Won, Lost

    estimated_value = Column(
        Numeric(12, 2),
        default=0
    )

    expected_close_date = Column(
        Date,
        nullable=True
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
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

    customer = relationship("Customer")
    assigned_user = relationship("User")