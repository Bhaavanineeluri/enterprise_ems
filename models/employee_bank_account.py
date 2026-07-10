from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeBankAccount(Base):
    __tablename__="employee_bank_accounts"

    id=Column(Integer,primary_key=True)

    employee_id=Column(Integer,ForeignKey("employees.id"))

    bank_name=Column(String(150))
    account_number=Column(String(50))
    ifsc_code=Column(String(20))
    branch_name=Column(String(150))

    is_primary=Column(Boolean,default=False)

    remarks=Column(String(255))

    created_by=Column(Integer)
    updated_by=Column(Integer)

    employee=relationship("Employee",back_populates="employee_bank_accounts")

    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())