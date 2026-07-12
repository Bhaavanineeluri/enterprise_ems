from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.employee import EmployeeUpdate, EmployeeResponse
from schemas.attendance import AttendanceCreate
from schemas.leave import LeaveCreate
from schemas.payroll import PayrollCreate
from schemas.performance_review import PerformanceReviewCreate

from services.employee import (
    update_employee,
    get_employees,
    get_employee,
    create_attendance,
    get_attendance,
    create_leave,
    get_leaves,
    create_payroll,
    get_payrolls,
    create_performance_review,
    get_performance_reviews,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# =====================================================
# EMPLOYEES
# =====================================================

@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("employee", "update"))
    ]
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


@router.get(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("employee", "view"))
    ]
)
def employees(
    db: Session = Depends(get_db)
):
    return get_employees(db)


@router.get(
    "/{employee_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("employee", "view"))
    ]
)
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

@router.post(
    "/attendance",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("attendance", "create"))
    ]
)
def attendance(
    data: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return create_attendance(
        db,
        data
    )


@router.get(
    "/attendance/all",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("attendance", "view"))
    ]
)
def attendance_list(
    db: Session = Depends(get_db)
):
    return get_attendance(db)


# =====================================================
# LEAVE
# =====================================================

@router.post(
    "/leave",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("leave", "create"))
    ]
)
def leave(
    data: LeaveCreate,
    db: Session = Depends(get_db)
):
    return create_leave(
        db,
        data
    )


@router.get(
    "/leave/all",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("leave", "view"))
    ]
)
def leave_list(
    db: Session = Depends(get_db)
):
    return get_leaves(db)


# =====================================================
# PAYROLL
# =====================================================

@router.post(
    "/payroll",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("payroll", "create"))
    ]
)
def payroll(
    data: PayrollCreate,
    db: Session = Depends(get_db)
):
    return create_payroll(
        db,
        data
    )


@router.get(
    "/payroll/all",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("payroll", "view"))
    ]
)
def payroll_list(
    db: Session = Depends(get_db)
):
    return get_payrolls(db)


# =====================================================
# PERFORMANCE REVIEW
# =====================================================

@router.post(
    "/performance-review",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("performance_review", "create"))
    ]
)
def performance_review(
    data: PerformanceReviewCreate,
    db: Session = Depends(get_db)
):
    return create_performance_review(
        db,
        data
    )


@router.get(
    "/performance-review/all",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("performance_review", "view"))
    ]
)
def performance_reviews(
    db: Session = Depends(get_db)
):
    return get_performance_reviews(db)


@router.delete(
    "/{employee_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("employee", "delete"))
    ]
)
def delete(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return delete_employee(
        db,
        employee_id
    )