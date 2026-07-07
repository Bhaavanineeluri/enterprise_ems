from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Approval(Base):

    __tablename__ = "approvals"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_id = Column(
        Integer,
        ForeignKey("workflows.id"),
        nullable=False
    )

    requested_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    approved_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    status = Column(
        String(30),
        default="Pending"
    )

    level = Column(
        Integer,
        default=1
    )

    remarks = Column(
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