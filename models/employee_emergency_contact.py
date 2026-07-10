from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeEmergencyContact(Base):
    __tablename__="employee_emergency_contacts"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    name=Column(String(150))
    relationship_name=Column(String(100))
    phone=Column(String(20))

    is_primary=Column(Boolean,default=True)

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_emergency_contacts")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())