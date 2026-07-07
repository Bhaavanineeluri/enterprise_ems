from sqlalchemy.orm import Session

from models.workflow import Workflow


class WorkflowRepository:


    def create(
        self,
        db: Session,
        workflow: Workflow
    ):

        db.add(workflow)
        db.commit()
        db.refresh(workflow)

        return workflow


    def get_all(
        self,
        db: Session
    ):

        return db.query(Workflow).all()


    def get(
        self,
        db: Session,
        workflow_id: int
    ):

        return db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()


workflow_repository = WorkflowRepository()