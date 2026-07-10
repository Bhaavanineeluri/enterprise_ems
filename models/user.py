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
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    role = Column(String(50), default="customer")

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    mfa_enabled = Column(Boolean, default=True)

    # Company Isolation (Multi-Company Architecture)
    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.id")
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    team_id = Column(
        Integer,
        ForeignKey("teams.id")
    )

    # Relationships
    company = relationship(
        "Company",
        back_populates="users"
    )

    branch = relationship(
        "Branch",
        back_populates="users"
    )

    department = relationship(
        "Department",
        back_populates="users"
    )

    team = relationship(
        "Team",
        back_populates="users"
    )

    

    customer = relationship(
        "Customer",
        back_populates="user",
        uselist=False
    )

    employee = relationship(
        "Employee",
        back_populates="user",
        uselist=False
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