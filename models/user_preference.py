from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class UserPreference(Base):

    __tablename__ = "user_preferences"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    theme = Column(
        String(20),
        default="light"
    )

    language = Column(
        String(20),
        default="en"
    )

    timezone = Column(
        String(50),
        default="UTC"
    )

    date_format = Column(
        String(20),
        default="YYYY-MM-DD"
    )

    email_notifications = Column(
        Boolean,
        default=True
    )

    sms_notifications = Column(
        Boolean,
        default=False
    )

    push_notifications = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship(
        "User",
        back_populates="preferences"
    )