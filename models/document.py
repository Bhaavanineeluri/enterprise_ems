from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Document(Base):

    __tablename__ = "documents"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    document_name = Column(
        String(255),
        nullable=False
    )


    document_type = Column(
        String(50),
        nullable=False
    )


    file_path = Column(
        String(500),
        nullable=False
    )


    is_public = Column(
        Boolean,
        default=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )