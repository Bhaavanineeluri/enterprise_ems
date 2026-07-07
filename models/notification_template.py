from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class NotificationTemplate(Base):

    __tablename__ = "notification_templates"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(100),
        unique=True,
        nullable=False
    )


    channel = Column(
        String(30),
        nullable=False
    )
    # EMAIL / SMS / PUSH / WEBHOOK


    subject = Column(
        String(255)
    )


    message = Column(
        Text,
        nullable=False
    )


    is_active = Column(
        Boolean,
        default=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )