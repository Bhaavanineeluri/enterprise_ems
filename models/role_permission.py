from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class RolePermission(Base):

    __tablename__ = "role_permissions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False
    )


    resource_id = Column(
        Integer,
        ForeignKey("resources.id"),
        nullable=False
    )


    permission_id = Column(
        Integer,
        ForeignKey("permissions.id"),
        nullable=False
    )


    role = relationship(
        "Role"
    )


    resource = relationship(
        "Resource"
    )


    permission = relationship(
        "Permission"
    )