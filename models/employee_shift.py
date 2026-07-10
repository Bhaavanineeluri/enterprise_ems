from sqlalchemy import Column,Integer,String,Time,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeShift(Base):
    __tablename__="employee_shifts"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    shift_name=Column(String(100))

    start_time=Column(Time)
    end_time=Column(Time)

    is_active=Column(Boolean,default=True)

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_shifts")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())