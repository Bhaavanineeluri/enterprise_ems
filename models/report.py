from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text
)

from sqlalchemy.sql import func

from database import Base



class Report(Base):

    __tablename__ = "reports"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    report_name = Column(
        String(100),
        nullable=False
    )


    report_type = Column(
        String(50),
        nullable=False
    )


    generated_by = Column(
        String(100),
        nullable=False
    )


    # Dynamic report filters
    filters = Column(
        Text,
        nullable=True
    )


    # Generated file location
    file_path = Column(
        String(500),
        nullable=True
    )


    # Export format
    export_format = Column(
        String(20),
        nullable=True
    )


    status = Column(
        String(30),
        default="Generated"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )