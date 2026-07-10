from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeContact(Base):
    __tablename__="employee_contacts"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    phone=Column(String(20))
    alternate_phone=Column(String(20))
    personal_email=Column(String(150))
    office_email=Column(String(150))

    is_active=Column(Boolean,default=True)

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_contacts")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())