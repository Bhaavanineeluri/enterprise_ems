from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class DocumentAccess(Base):

    __tablename__ = "document_access"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    can_view = Column(
        Boolean,
        default=True
    )


    can_edit = Column(
        Boolean,
        default=False
    )


    can_delete = Column(
        Boolean,
        default=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )