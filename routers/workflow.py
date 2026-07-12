from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.workflow import WorkflowCreate
from schemas.approval import (
    ApprovalCreate,
    ApprovalUpdate
)
from schemas.workflow_escalation import (
    WorkflowEscalationCreate
)
from schemas.workflow_sla import (
    WorkflowSLACreate
)

from services.workflow import (
    create_workflow,
    get_workflows,
    create_approval,
    update_approval,
    get_approvals,
    create_escalation,
    get_escalations,
    create_sla,
    get_slas
)

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow Engine"]
)


# =====================================================
# WORKFLOW
# =====================================================

@router.post(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "create"))
    ]
)
def add_workflow(
    data: WorkflowCreate,
    db: Session = Depends(get_db)
):
    return create_workflow(db, data)


@router.get(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "view"))
    ]
)
def list_workflows(
    db: Session = Depends(get_db)
):
    return get_workflows(db)


# =====================================================
# APPROVAL
# =====================================================

@router.post(
    "/approval",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "approve"))
    ]
)
def add_approval(
    data: ApprovalCreate,
    db: Session = Depends(get_db)
):
    return create_approval(db, data)


@router.put(
    "/approval/{approval_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "approve"))
    ]
)
def approve_request(
    approval_id: int,
    data: ApprovalUpdate,
    db: Session = Depends(get_db)
):
    return update_approval(
        db,
        approval_id,
        data
    )


@router.get(
    "/approval",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "view"))
    ]
)
def list_approvals(
    db: Session = Depends(get_db)
):
    return get_approvals(db)


# =====================================================
# ESCALATION
# =====================================================

@router.post(
    "/escalation",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "manage"))
    ]
)
def add_escalation(
    data: WorkflowEscalationCreate,
    db: Session = Depends(get_db)
):
    return create_escalation(db, data)


@router.get(
    "/escalation",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "view"))
    ]
)
def list_escalations(
    db: Session = Depends(get_db)
):
    return get_escalations(db)


# =====================================================
# SLA
# =====================================================

@router.post(
    "/sla",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "manage"))
    ]
)
def add_sla(
    data: WorkflowSLACreate,
    db: Session = Depends(get_db)
):
    return create_sla(db, data)


@router.get(
    "/sla",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("workflow", "view"))
    ]
)
def list_sla(
    db: Session = Depends(get_db)
):
    return get_slas(db)