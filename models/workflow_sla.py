from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class WorkflowSLA(Base):

    __tablename__ = "workflow_slas"


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


    approval_level = Column(
        Integer,
        default=1
    )


    allowed_hours = Column(
        Integer,
        nullable=False
    )


    action = Column(
        String(100),
        default="ESCALATE"
    )