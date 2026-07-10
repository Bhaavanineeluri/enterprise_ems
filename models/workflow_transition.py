from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class WorkflowTransition(Base):
    __tablename__ = "workflow_transitions"

    id = Column(Integer, primary_key=True)

    workflow_id = Column(
        Integer,
        ForeignKey("workflow_definitions.id")
    )

    from_step = Column(
        Integer,
        ForeignKey("workflow_steps.id")
    )

    to_step = Column(
        Integer,
        ForeignKey("workflow_steps.id")
    )