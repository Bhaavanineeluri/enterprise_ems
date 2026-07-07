from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)

    team_name = Column(String(150), nullable=False)
    team_code = Column(String(50), nullable=False, unique=True)

    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)

    # FK → Department
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    department = relationship("Department", back_populates="teams")

    # FK → Users (MUST match User.team)
    users = relationship("User", back_populates="team")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())