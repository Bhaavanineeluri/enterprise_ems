from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.workflow import WorkflowCreate
from schemas.approval import (
    ApprovalCreate,
    ApprovalUpdate
)

from services.workflow import (
    create_workflow,
    get_workflows,
    create_approval,
    update_approval,
    get_approvals
)


router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)


# =====================================================
# WORKFLOW
# =====================================================


@router.post("/")
def add_workflow(
    data: WorkflowCreate,
    db: Session = Depends(get_db)
):

    return create_workflow(
        db,
        data
    )



@router.get("/")
def list_workflows(
    db: Session = Depends(get_db)
):

    return get_workflows(db)



# =====================================================
# APPROVAL
# =====================================================


@router.post("/approval")
def add_approval(
    data: ApprovalCreate,
    db: Session = Depends(get_db)
):

    return create_approval(
        db,
        data
    )



@router.put("/approval/{approval_id}")
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



@router.get("/approval")
def list_approvals(
    db: Session = Depends(get_db)
):

    return get_approvals(db)