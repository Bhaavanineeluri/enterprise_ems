from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from models.user import User
from models.attendance import Attendance
from models.leave import Leave
from models.payroll import Payroll
from models.performance_review import PerformanceReview

from repositories.employee import employee_repository
from repositories.attendance import attendance_repository
from repositories.leave import leave_repository
from repositories.payroll import payroll_repository
from repositories.performance_review import performance_review_repository
from core.unit_of_work import UnitOfWork

# =====================================================
# EMPLOYEE
# =====================================================

def get_employees(db: Session):

    return employee_repository.get_all(db)


def get_employee(
    db: Session,
    employee_id: int
):

    employee = employee_repository.get(
        db,
        employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# =====================================================
# ATTENDANCE
# =====================================================

def create_attendance(
    db: Session,
    data
):

    employee = employee_repository.get(
        db,
        data.employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    attendance = Attendance(**data.model_dump())

    return attendance_repository.create(
        db,
        attendance
    )


def get_attendance(db: Session):

    return attendance_repository.get_all(db)


# =====================================================
# LEAVE
# =====================================================

def create_leave(
    db: Session,
    data
):

    employee = employee_repository.get(
        db,
        data.employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    leave = Leave(**data.model_dump())

    return leave_repository.create(
        db,
        leave
    )


def get_leaves(db: Session):

    return leave_repository.get_all(db)


# =====================================================
# PAYROLL
# =====================================================

def create_payroll(
    db: Session,
    data
):

    employee = employee_repository.get(
        db,
        data.employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    payroll = Payroll(**data.model_dump())

    return payroll_repository.create(
        db,
        payroll
    )


def get_payrolls(db: Session):

    return payroll_repository.get_all(db)


# =====================================================
# PERFORMANCE REVIEW
# =====================================================

def create_performance_review(
    db: Session,
    data
):

    employee = employee_repository.get(
        db,
        data.employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    review = PerformanceReview(**data.model_dump())

    return performance_review_repository.create(
        db,
        review
    )


def get_performance_reviews(db: Session):

    return performance_review_repository.get_all(db)
# =====================================================
# DELETE EMPLOYEE
# =====================================================

def delete_employee(
    db: Session,
    employee_id: int
):

    uow = UnitOfWork(db)

    employee = uow.employees.get(
        db,
        employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    try:

        uow.employees.delete(
            db,
            employee
        )

        uow.commit()

        return {
            "success": True,
            "message": "Employee deleted successfully"
        }

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
def update_employee(
    employee_id: int,
    employee_data,
    db: Session
):
    db_employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not db_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    update_data = employee_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_employee,
            key,
            value
        )

    db.commit()
    db.refresh(db_employee)

    return db_employee