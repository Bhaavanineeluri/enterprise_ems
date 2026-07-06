from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.user import User
from models.company import Company
from models.branch import Branch
from models.department import Department
from models.team import Team


def assign_user(
    db: Session,
    user_id: int,
    company_id: int = None,
    branch_id: int = None,
    department_id: int = None,
    team_id: int = None
):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Validate company
    if company_id:
        company = db.query(Company).filter(Company.id == company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        user.company_id = company_id

    # Validate branch
    if branch_id:
        branch = db.query(Branch).filter(Branch.id == branch_id).first()
        if not branch:
            raise HTTPException(status_code=404, detail="Branch not found")
        user.branch_id = branch_id

    # Validate department
    if department_id:
        dept = db.query(Department).filter(Department.id == department_id).first()
        if not dept:
            raise HTTPException(status_code=404, detail="Department not found")
        user.department_id = department_id

    # Validate team
    if team_id:
        team = db.query(Team).filter(Team.id == team_id).first()
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        user.team_id = team_id

    db.commit()
    db.refresh(user)

    return user