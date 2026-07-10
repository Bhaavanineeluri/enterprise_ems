from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    employee_code = Column(String(20), unique=True, nullable=True)
    designation = Column(String(100), nullable=True)

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=True
    )

    # ==========================
    # Existing Relationships
    # ==========================

    user = relationship(
        "User",
        back_populates="employee"
    )

    department = relationship("Department")

    # ==========================
    # Employee Module
    # ==========================

    employee_addresses = relationship(
        "EmployeeAddress",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_contacts = relationship(
        "EmployeeContact",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_bank_accounts = relationship(
        "EmployeeBankAccount",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_documents = relationship(
        "EmployeeDocument",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_certifications = relationship(
        "EmployeeCertification",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_trainings = relationship(
        "EmployeeTraining",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_assets = relationship(
        "EmployeeAsset",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_salaries = relationship(
        "EmployeeSalary",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_shifts = relationship(
        "EmployeeShift",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    employee_emergency_contacts = relationship(
        "EmployeeEmergencyContact",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )