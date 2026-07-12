from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100)
    )

    company_name = Column(
        String(150)
    )

    email = Column(
        String(150),
        nullable=False,
        unique=True
    )

    phone = Column(
        String(20)
    )

    source = Column(
        String(50)
    )
    # Website, Referral, LinkedIn, Advertisement...

    status = Column(
        String(30),
        default="New"
    )
    # New, Contacted, Qualified, Converted, Lost

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

    assigned_user = relationship(
        "User"
    )