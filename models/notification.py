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


class Notification(Base):

    __tablename__ = "notifications"


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


    template_id = Column(
        Integer,
        ForeignKey("notification_templates.id"),
        nullable=True
    )


    channel = Column(
        String(30),
        nullable=False
    )


    message = Column(
        Text,
        nullable=False
    )


    status = Column(
        String(30),
        default="Pending"
    )


    sent_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )