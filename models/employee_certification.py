from sqlalchemy import Column,Integer,String,Date,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeCertification(Base):
    __tablename__="employee_certifications"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    certification_name=Column(String(150))
    provider=Column(String(150))

    issue_date=Column(Date)
    expiry_date=Column(Date)

    certificate_number=Column(String(100))

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_certifications")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())