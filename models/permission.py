from sqlalchemy import (
    Column,
    Integer,
    String
)

from database import Base


class Permission(Base):

    __tablename__ = "permissions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    action = Column(
        String(50),
        unique=True,
        nullable=False
    )