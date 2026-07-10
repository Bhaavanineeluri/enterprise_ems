from sqlalchemy import Column,Integer,String,Date,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeTraining(Base):
    __tablename__="employee_trainings"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    training_name=Column(String(150))
    trainer=Column(String(150))

    training_date=Column(Date)

    status=Column(String(50))

    is_completed=Column(Boolean,default=False)

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_trainings")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())