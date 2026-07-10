from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Payroll(Base):

    __tablename__ = "payroll"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    basic_salary = Column(
        Float,
        default=0
    )

    payment_status = Column(
        String(30),
        default="Pending"
    )

    bank_name = Column(
        String(100)
    )

    account_number = Column(
        String(50)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )