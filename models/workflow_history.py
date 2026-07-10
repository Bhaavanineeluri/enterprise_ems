from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class WorkflowHistory(Base):
    __tablename__ = "workflow_histories"

    id = Column(Integer, primary_key=True)

    workflow_instance_id = Column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    action = Column(String(100))

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())