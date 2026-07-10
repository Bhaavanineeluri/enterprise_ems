from repositories.base import BaseRepository

from models.workflow_escalation import WorkflowEscalation


workflow_escalation_repository = BaseRepository(
    WorkflowEscalation
)