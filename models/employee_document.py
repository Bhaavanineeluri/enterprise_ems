from sqlalchemy import Column,Integer,String,Date,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeDocument(Base):
    __tablename__="employee_documents"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    document_type=Column(String(100))
    document_number=Column(String(100))

    issue_date=Column(Date)
    expiry_date=Column(Date)

    file_path=Column(String(255))

    is_verified=Column(Boolean,default=False)

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_documents")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())