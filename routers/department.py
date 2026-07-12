from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.department import DepartmentCreate, DepartmentResponse
from services.department import (
    create_department,
    get_all_departments,
    get_department,
    delete_department
)

router = APIRouter(
    prefix="/departments",
    tags=["Department"]
)


@router.post(
    "/",
    response_model=DepartmentResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("department", "create"))
    ]
)
def create(
    data: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department(db, data)


@router.get(
    "/",
    response_model=list[DepartmentResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("department", "view"))
    ]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_departments(db)


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("department", "view"))
    ]
)
def get_one(
    department_id: int,
    db: Session = Depends(get_db)
):
    return get_department(db, department_id)


@router.delete(
    "/{department_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("department", "delete"))
    ]
)
def delete(
    department_id: int,
    db: Session = Depends(get_db)
):
    return delete_department(
        db,
        department_id
    )