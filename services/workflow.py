from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.workflow import Workflow
from models.approval import Approval

from repositories.workflow import workflow_repository
from repositories.approval import approval_repository

from schemas.workflow import WorkflowCreate
from schemas.approval import (
    ApprovalCreate,
    ApprovalUpdate
)



# =====================================================
# WORKFLOW
# =====================================================


def create_workflow(
    db: Session,
    data: WorkflowCreate
):

    existing = db.query(Workflow).filter(
        Workflow.name == data.name
    ).first()


    if existing:
        raise HTTPException(
            status_code=400,
            detail="Workflow already exists"
        )


    workflow = Workflow(
        name=data.name,
        module=data.module,
        description=data.description
    )


    return workflow_repository.create(
        db,
        workflow
    )



def get_workflows(
    db: Session
):

    return workflow_repository.get_all(db)



# =====================================================
# APPROVAL
# =====================================================


def create_approval(
    db: Session,
    data: ApprovalCreate
):

    workflow = workflow_repository.get(
        db,
        data.workflow_id
    )


    if not workflow:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )


    approval = Approval(
        workflow_id=data.workflow_id,
        requested_by=data.requested_by,
        level=data.level
    )


    return approval_repository.create(
        db,
        approval
    )



def update_approval(
    db: Session,
    approval_id: int,
    data: ApprovalUpdate
):

    approval = approval_repository.get(
        db,
        approval_id
    )


    if not approval:
        raise HTTPException(
            status_code=404,
            detail="Approval not found"
        )


    approval.status = data.status
    approval.approved_by = data.approved_by
    approval.remarks = data.remarks


    return approval_repository.update(
        db,
        approval
    )



def get_approvals(
    db: Session
):

    return approval_repository.get_all(db)