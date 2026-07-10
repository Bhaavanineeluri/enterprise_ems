from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Attendance(Base):

    __tablename__ = "attendance"

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

    attendance_date = Column(
        Date,
        nullable=False
    )

    check_in = Column(
        String(20)
    )

    check_out = Column(
        String(20)
    )

    status = Column(
        String(30),
        default="Present"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )