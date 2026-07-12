from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.branch import BranchCreate, BranchResponse
from services.branch import (
    create_branch,
    get_all_branches,
    get_branch,
    delete_branch
)

router = APIRouter(
    prefix="/branches",
    tags=["Branch"]
)


@router.post(
    "/",
    response_model=BranchResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("branch", "create"))
    ]
)
def create(
    data: BranchCreate,
    db: Session = Depends(get_db)
):
    return create_branch(db, data)


@router.get(
    "/",
    response_model=list[BranchResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("branch", "view"))
    ]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_branches(db)


@router.get(
    "/{branch_id}",
    response_model=BranchResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("branch", "view"))
    ]
)
def get_one(
    branch_id: int,
    db: Session = Depends(get_db)
):
    return get_branch(db, branch_id)


@router.delete(
    "/{branch_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("branch", "delete"))
    ]
)
def delete(
    branch_id: int,
    db: Session = Depends(get_db)
):
    return delete_branch(
        db,
        branch_id
    )