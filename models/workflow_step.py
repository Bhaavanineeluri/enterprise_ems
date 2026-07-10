from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(Integer, primary_key=True)

    workflow_id = Column(
        Integer,
        ForeignKey("workflow_definitions.id")
    )

    step_name = Column(String(100))

    step_order = Column(Integer)

    workflow = relationship(
        "WorkflowDefinition",
        back_populates="steps"
    )