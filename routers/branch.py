from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.branch import BranchCreate, BranchResponse
from services.branch import create_branch, get_all_branches, get_branch

router = APIRouter(prefix="/branches", tags=["Branch"])


@router.post("/", response_model=BranchResponse)
def create(data: BranchCreate, db: Session = Depends(get_db)):
    return create_branch(db, data)


@router.get("/", response_model=list[BranchResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_branches(db)


@router.get("/{branch_id}", response_model=BranchResponse)
def get_one(branch_id: int, db: Session = Depends(get_db)):
    return get_branch(db, branch_id)