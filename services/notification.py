from datetime import datetime, UTC

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.notification import Notification
from models.notification_template import NotificationTemplate

from repositories.notification import (
    notification_repository
)

from schemas.notification import (
    NotificationCreate
)



# =====================================================
# SEND NOTIFICATION
# =====================================================


def send_notification(
    db: Session,
    data: NotificationCreate
):


    notification = Notification(

        user_id=data.user_id,

        template_id=data.template_id,

        channel=data.channel,

        message=data.message,

        status="Sent",

        sent_at=datetime.now(UTC)

    )


    return notification_repository.create(
        db,
        notification
    )



# =====================================================
# GET NOTIFICATIONS
# =====================================================


def get_notifications(
    db: Session
):

    return notification_repository.get_all(db)



# =====================================================
# CREATE TEMPLATE
# =====================================================


def create_template(
    db: Session,
    data
):


    existing = db.query(
        NotificationTemplate
    ).filter(
        NotificationTemplate.name == data.name
    ).first()


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Template already exists"
        )



    template = NotificationTemplate(
        name=data.name,
        channel=data.channel,
        subject=data.subject,
        message=data.message
    )


    return notification_repository.create_template(
        db,
        template
    )