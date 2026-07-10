from repositories.base import BaseRepository

from models.workflow_sla import WorkflowSLA


workflow_sla_repository = BaseRepository(
    WorkflowSLA
)