from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.attendance import AttendanceCreate
from schemas.leave import LeaveCreate
from schemas.payroll import PayrollCreate
from schemas.performance_review import (
    PerformanceReviewCreate
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from database import get_db
from dependencies.auth import get_current_user

from schemas.employee import EmployeeUpdate, EmployeeResponse
from services.employee import update_employee
from services.employee import (
    get_employees,
    get_employee,
    create_attendance,
    get_attendance,
    create_leave,
    get_leaves,
    create_payroll,
    get_payrolls,
    create_performance_review,
    get_performance_reviews,delete_employee
)


router = APIRouter(
    prefix="/employees",
    tags=["Employee Management"]
)


# =====================================================
# EMPLOYEES
# =====================================================



router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee_details(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    return update_employee(
        employee_id,
        employee,
        db
    )
@router.get("/")
def employees(
    db: Session = Depends(get_db)
):
    return get_employees(db)


@router.get("/{employee_id}")
def employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return get_employee(
        db,
        employee_id
    )


# =====================================================
# ATTENDANCE
# =====================================================

@router.post("/attendance")
def attendance(
    data: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return create_attendance(
        db,
        data
    )


@router.get("/attendance/all")
def attendance_list(
    db: Session = Depends(get_db)
):
    return get_attendance(db)


# =====================================================
# LEAVE
# =====================================================

@router.post("/leave")
def leave(
    data: LeaveCreate,
    db: Session = Depends(get_db)
):
    return create_leave(
        db,
        data
    )


@router.get("/leave/all")
def leave_list(
    db: Session = Depends(get_db)
):
    return get_leaves(db)


# =====================================================
# PAYROLL
# =====================================================

@router.post("/payroll")
def payroll(
    data: PayrollCreate,
    db: Session = Depends(get_db)
):
    return create_payroll(
        db,
        data
    )


@router.get("/payroll/all")
def payroll_list(
    db: Session = Depends(get_db)
):
    return get_payrolls(db)


# =====================================================
# PERFORMANCE REVIEW
# =====================================================

@router.post("/performance-review")
def performance_review(
    data: PerformanceReviewCreate,
    db: Session = Depends(get_db)
):
    return create_performance_review(
        db,
        data
    )


@router.get("/performance-review/all")
def performance_reviews(
    db: Session = Depends(get_db)
):
    return get_performance_reviews(db)


@router.delete("/{employee_id}")
def delete(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return delete_employee(
        db,
        employee_id
    )