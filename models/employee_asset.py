from sqlalchemy import Column,Integer,String,Date,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeAsset(Base):
    __tablename__="employee_assets"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    asset_name=Column(String(150))
    asset_code=Column(String(100))

    issue_date=Column(Date)
    return_date=Column(Date)

    status=Column(String(50))

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_assets")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())