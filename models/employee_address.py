from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class EmployeeAddress(Base):
    __tablename__ = "employee_addresses"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    address_type = Column(String(30))
    address = Column(String(255))

    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    zipcode = Column(String(20))

    is_primary = Column(Boolean, default=False)
    remarks = Column(String(255))

    created_by = Column(Integer)
    updated_by = Column(Integer)

    employee = relationship("Employee", back_populates="employee_addresses")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())