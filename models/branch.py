from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)

    branch_name = Column(String(150), nullable=False)
    branch_code = Column(String(50), nullable=False, unique=True)

    email = Column(String(150), nullable=True)
    phone = Column(String(20), nullable=True)

    address = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True)

    # -------------------------
    # Company Relationship
    # -------------------------
    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    company = relationship(
        "Company",
        back_populates="branches"
    )

    # -------------------------
    # Department Relationship
    # -------------------------
    departments = relationship(
        "Department",
        back_populates="branch",
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