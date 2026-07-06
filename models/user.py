from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    phone = Column(
        String(15),
        unique=True,
        nullable=False
    )

    password = Column(String(255), nullable=False)

    role = Column(String(50), default="customer")
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    is_active = Column(Boolean, default=True)

    is_verified = Column(Boolean, default=False)

    mfa_enabled = Column(Boolean, default=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=True,
        index=True
    )

    company = relationship(
        "Company",
        back_populates="users"
    )

    # ----------------------------
    # Customer Profile
    # ----------------------------
    customer = relationship(
        "Customer",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # ----------------------------
    # Employee Profile
    # ----------------------------
    employee = relationship(
        "Employee",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    company = relationship("Company", back_populates="users")

    branch = relationship("Branch")
    department = relationship("Department")
    team = relationship("Team")