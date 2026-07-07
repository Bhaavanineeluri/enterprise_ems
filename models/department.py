from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    department_name = Column(String(150), nullable=False)
    department_code = Column(String(50), nullable=False, unique=True)

    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)

    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)

    branch = relationship("Branch", back_populates="departments")

    teams = relationship(
        "Team",
        back_populates="department",
        cascade="all, delete-orphan"
    )

    # 🔥 REQUIRED FIX
    users = relationship(
        "User",
        back_populates="department"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )