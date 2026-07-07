from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String(150), nullable=False, unique=True)
    company_code = Column(String(50), nullable=False, unique=True)

    email = Column(String(150))
    phone = Column(String(20))
    website = Column(String(150))
    address = Column(String(255))

    is_active = Column(Boolean, default=True)

    users = relationship("User", back_populates="company")
    branches = relationship("Branch", back_populates="company", cascade="all, delete-orphan")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())