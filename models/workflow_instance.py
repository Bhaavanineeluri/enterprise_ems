from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class WorkflowInstance(Base):
    __tablename__ = "workflow_instances"

    id = Column(Integer, primary_key=True)

    workflow_id = Column(
        Integer,
        ForeignKey("workflow_definitions.id")
    )

    reference_id = Column(Integer)

    status = Column(String(50))

    tasks = relationship(
        "WorkflowTask",
        back_populates="instance"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())