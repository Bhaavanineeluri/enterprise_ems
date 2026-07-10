from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.workflow import Workflow
from models.approval import Approval
from services.notification import send_notification

from schemas.notification import NotificationCreate
from repositories.workflow import workflow_repository
from repositories.approval import approval_repository

from schemas.workflow import WorkflowCreate
from schemas.approval import (
    ApprovalCreate,
    ApprovalUpdate
)
from models.workflow_sla import WorkflowSLA

from repositories.workflow_sla import (
    workflow_sla_repository
)

from schemas.workflow_sla import (
    WorkflowSLACreate
)
from models.workflow_escalation import WorkflowEscalation

from repositories.workflow_escalation import (
    workflow_escalation_repository
)

from schemas.workflow_escalation import (
    WorkflowEscalationCreate
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
        approval_level=data.approval_level
    )


    approval = approval_repository.create(
        db,
        approval
    )


    notification = NotificationCreate(
        user_id=data.requested_by,
        template_id=None,
        channel="IN_APP",
        message=f"New approval request created for {workflow.name}"
    )


    send_notification(
        db,
        notification
    )


    return approval

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

    updated_approval = approval_repository.update(
        db,
        approval
    )

    notification = NotificationCreate(
        user_id=approval.requested_by,
        template_id=None,
        channel="IN_APP",
        message=f"Your approval request status changed to {approval.status}"
    )

    send_notification(
        db,
        notification
    )

    return updated_approval


def get_approvals(
    db: Session
):

    return approval_repository.get_all(db)
# =====================================================
# ESCALATION
# =====================================================


def create_escalation(
    db: Session,
    data: WorkflowEscalationCreate
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


    escalation = WorkflowEscalation(
        **data.model_dump()
    )


    return workflow_escalation_repository.create(
        db,
        escalation
    )



def get_escalations(
    db: Session
):

    return workflow_escalation_repository.get_all(
        db
    )
def create_sla(
    db: Session,
    data: WorkflowSLACreate
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


    sla = WorkflowSLA(
        **data.model_dump()
    )


    return workflow_sla_repository.create(
        db,
        sla
    )



def get_slas(
    db: Session
):

    return workflow_sla_repository.get_all(
        db
    )