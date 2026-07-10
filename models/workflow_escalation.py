from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class WorkflowEscalation(Base):

    __tablename__ = "workflow_escalations"


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


    level = Column(
        Integer,
        default=1
    )


    after_hours = Column(
        Integer,
        nullable=False
    )


    escalate_to = Column(
        String(100),
        nullable=False
    )


    status = Column(
        String(30),
        default="ACTIVE"
    )