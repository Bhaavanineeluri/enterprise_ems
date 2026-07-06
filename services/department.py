from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.department import Department
from models.branch import Branch
from schemas.department import DepartmentCreate


def create_department(db: Session, data: DepartmentCreate):

    branch = db.query(Branch).filter(
        Branch.id == data.branch_id
    ).first()

    if not branch:
        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )

    existing = db.query(Department).filter(
        Department.department_code == data.department_code
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Department code already exists"
        )

    department = Department(
        department_name=data.department_name,
        department_code=data.department_code,
        description=data.description,
        branch_id=data.branch_id
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department


def get_all_departments(db: Session):
    return db.query(Department).all()


def get_department(db: Session, department_id: int):

    department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department