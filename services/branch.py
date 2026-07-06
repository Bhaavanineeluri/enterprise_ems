from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.branch import Branch
from models.company import Company
from schemas.branch import BranchCreate


def create_branch(db: Session, data: BranchCreate):

    company = db.query(Company).filter(
        Company.id == data.company_id
    ).first()

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    existing = db.query(Branch).filter(
        Branch.branch_code == data.branch_code
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Branch code already exists"
        )

    branch = Branch(
        branch_name=data.branch_name,
        branch_code=data.branch_code,
        email=data.email,
        phone=data.phone,
        address=data.address,
        company_id=data.company_id
    )

    db.add(branch)
    db.commit()
    db.refresh(branch)

    return branch


def get_all_branches(db: Session):
    return db.query(Branch).all()


def get_branch(db: Session, branch_id: int):

    branch = db.query(Branch).filter(
        Branch.id == branch_id
    ).first()

    if not branch:
        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )

    return branch