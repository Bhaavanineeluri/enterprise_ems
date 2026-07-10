from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from database import Base


class NotificationWebhook(Base):

    __tablename__ = "notification_webhooks"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    event = Column(
        String(100),
        nullable=False
    )


    url = Column(
        String(255),
        nullable=False
    )


    is_active = Column(
        Boolean,
        default=True
    )