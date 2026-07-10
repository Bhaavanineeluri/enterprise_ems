from datetime import datetime, UTC

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.notification import Notification
from models.notification_template import NotificationTemplate

from repositories.notification import (
    notification_repository
)
from services.notification_channels.email import send_email
from services.notification_channels.sms import send_sms
from services.notification_channels.push import send_push
from models.notification_webhook import NotificationWebhook

from repositories.notification_webhook import (
    notification_webhook_repository
)

from schemas.notification_webhook import (
    NotificationWebhookCreate,
    NotificationWebhookUpdate
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

    notification = notification_repository.create(
        db,
        notification
    )

    if data.channel == "EMAIL":

        send_email(
            recipient=str(data.user_id),
            subject="Notification",
            message=data.message
        )


    elif data.channel == "SMS":

        send_sms(
            phone=str(data.user_id),
            message=data.message
        )


    elif data.channel == "PUSH":

        send_push(
            user_id=data.user_id,
            message=data.message
        )


    return notification
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


def get_templates(
    db: Session
):

    return (
        db.query(NotificationTemplate)
        .all()
    )



def update_template(
    db: Session,
    template_id: int,
    data
):

    template = (
        db.query(NotificationTemplate)
        .filter(
            NotificationTemplate.id == template_id
        )
        .first()
    )


    if not template:

        raise HTTPException(
            status_code=404,
            detail="Template not found"
        )


    update_data = data.model_dump(
        exclude_unset=True
    )


    for key, value in update_data.items():

        setattr(
            template,
            key,
            value
        )


    db.commit()
    db.refresh(template)


    return template



def delete_template(
    db: Session,
    template_id: int
):

    template = (
        db.query(NotificationTemplate)
        .filter(
            NotificationTemplate.id == template_id
        )
        .first()
    )


    if not template:

        raise HTTPException(
            status_code=404,
            detail="Template not found"
        )


    template.is_active = False


    db.commit()


    return {
        "message": "Template disabled successfully"
    }
# =====================================================
# WEBHOOK MANAGEMENT
# =====================================================


def create_webhook(
    db: Session,
    data: NotificationWebhookCreate
):

    webhook = NotificationWebhook(
        event=data.event,
        url=data.url
    )


    return notification_webhook_repository.create(
        db,
        webhook
    )



def get_webhooks(
    db: Session
):

    return notification_webhook_repository.get_all(
        db
    )



def update_webhook(
    db: Session,
    webhook_id: int,
    data: NotificationWebhookUpdate
):

    webhook = notification_webhook_repository.get(
        db,
        webhook_id
    )


    if not webhook:

        raise HTTPException(
            status_code=404,
            detail="Webhook not found"
        )


    update_data = data.model_dump(
        exclude_unset=True
    )


    for key, value in update_data.items():

        setattr(
            webhook,
            key,
            value
        )


    return notification_webhook_repository.update(
        db,
        webhook
    )



def delete_webhook(
    db: Session,
    webhook_id: int
):

    webhook = notification_webhook_repository.get(
        db,
        webhook_id
    )


    if not webhook:

        raise HTTPException(
            status_code=404,
            detail="Webhook not found"
        )


    db.delete(webhook)

    db.commit()


    return {
        "message": "Webhook deleted successfully"
    }