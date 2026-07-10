from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class WorkflowAttachment(Base):
    __tablename__ = "workflow_attachments"

    id = Column(Integer, primary_key=True)

    workflow_instance_id = Column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    file_name = Column(String(255))

    file_path = Column(String(255))