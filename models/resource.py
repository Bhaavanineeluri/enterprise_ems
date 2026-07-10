from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), unique=True, nullable=False)

    role_permissions = relationship(
        "RolePermission",
        back_populates="resource"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )