from sqlalchemy import Column, Integer, Boolean, ForeignKey
from database import Base


class WorkflowNotification(Base):
    __tablename__ = "workflow_notifications"

    id = Column(Integer, primary_key=True)

    workflow_instance_id = Column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    is_sent = Column(Boolean, default=False)