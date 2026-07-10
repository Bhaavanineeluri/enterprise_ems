from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text
)

from sqlalchemy.sql import func

from database import Base


class DocumentVersion(Base):

    __tablename__ = "document_versions"


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


    version_number = Column(
        Integer,
        nullable=False
    )


    file_path = Column(
        String(500),
        nullable=False
    )


    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    change_notes = Column(
        Text,
        nullable=True
    )


    status = Column(
        String(50),
        default="ACTIVE"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )