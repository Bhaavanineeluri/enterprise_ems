from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class WorkflowComment(Base):
    __tablename__ = "workflow_comments"

    id = Column(Integer, primary_key=True)

    workflow_instance_id = Column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    comment = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())