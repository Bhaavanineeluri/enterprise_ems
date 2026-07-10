from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base


class WorkflowDefinition(Base):
    __tablename__ = "workflow_definitions"

    id = Column(Integer, primary_key=True)

    workflow_name = Column(String(150), nullable=False)
    module_name = Column(String(100), nullable=False)

    version = Column(Integer, default=1)

    is_active = Column(Boolean, default=True)

    steps = relationship(
        "WorkflowStep",
        back_populates="workflow"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())