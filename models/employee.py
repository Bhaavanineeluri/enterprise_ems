from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

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

    # OPTIONAL (recommended improvement)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    user = relationship(
        "User",
        back_populates="employee"
    )

    department = relationship("Department")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )