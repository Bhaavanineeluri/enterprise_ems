from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class WorkflowTask(Base):
    __tablename__ = "workflow_tasks"

    id = Column(Integer, primary_key=True)

    workflow_instance_id = Column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id")
    )

    status = Column(String(50))

    instance = relationship(
        "WorkflowInstance",
        back_populates="tasks"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())