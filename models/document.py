from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Text
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


    # Owner
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


    # File Details

    file_path = Column(
        String(500),
        nullable=False
    )


    file_extension = Column(
        String(20),
        nullable=True
    )


    file_size = Column(
        Integer,
        nullable=True
    )


    mime_type = Column(
        String(100),
        nullable=True
    )


    # Upload Information

    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    # Access Control

    is_public = Column(
        Boolean,
        default=False
    )


    access_level = Column(
        String(50),
        default="PRIVATE"
    )


    # Metadata

    description = Column(
        Text,
        nullable=True
    )


    tags = Column(
        String(500),
        nullable=True
    )


    # OCR Support

    ocr_text = Column(
        Text,
        nullable=True
    )


    ocr_completed = Column(
        Boolean,
        default=False
    )


    # Timestamps

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )