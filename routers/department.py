from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.department import DepartmentCreate, DepartmentResponse
from services.department import create_department, get_all_departments, get_department,delete_department

router = APIRouter(prefix="/departments", tags=["Department"])


@router.post("/", response_model=DepartmentResponse)
def create(data: DepartmentCreate, db: Session = Depends(get_db)):
    return create_department(db, data)


@router.get("/", response_model=list[DepartmentResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_departments(db)


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_one(department_id: int, db: Session = Depends(get_db)):
    return get_department(db, department_id)
@router.delete("/{department_id}")
def delete(
    department_id: int,
    db: Session = Depends(get_db)
):

    return delete_department(
        db,
        department_id
    )