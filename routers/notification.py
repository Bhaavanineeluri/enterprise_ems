from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.notification import (
    NotificationCreate,
    NotificationTemplateCreate
)
from schemas.notification import (
    NotificationTemplateUpdate
)
from schemas.notification_webhook import (
    NotificationWebhookCreate,
    NotificationWebhookUpdate
)


from services.notification import (
    create_webhook,
    get_webhooks,
    update_webhook,
    delete_webhook
)


from services.notification import (
    get_templates,
    update_template,
    delete_template
)

from services.notification import (
    send_notification,
    get_notifications,
    create_template
)


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# =====================================================
# SEND NOTIFICATION
# =====================================================

@router.post("/")
def create_notification(
    data: NotificationCreate,
    db: Session = Depends(get_db)
):

    return send_notification(
        db,
        data
    )



# =====================================================
# GET NOTIFICATIONS
# =====================================================

@router.get("/")
def list_notifications(
    db: Session = Depends(get_db)
):

    return get_notifications(db)



# =====================================================
# CREATE TEMPLATE
# =====================================================

@router.post("/templates")
def add_template(
    data: NotificationTemplateCreate,
    db: Session = Depends(get_db)
):

    return create_template(
        db,
        data
    )
# =====================================================
# TEMPLATE MANAGEMENT
# =====================================================


@router.get("/templates")
def list_templates(
    db: Session = Depends(get_db)
):

    return get_templates(db)



@router.put("/templates/{template_id}")
def edit_template(
    template_id: int,
    data: NotificationTemplateUpdate,
    db: Session = Depends(get_db)
):

    return update_template(
        db,
        template_id,
        data
    )



@router.delete("/templates/{template_id}")
def remove_template(
    template_id: int,
    db: Session = Depends(get_db)
):

    return delete_template(
        db,
        template_id
    )
# =====================================================
# WEBHOOK MANAGEMENT
# =====================================================


@router.post("/webhooks")
def add_webhook(
    data: NotificationWebhookCreate,
    db: Session = Depends(get_db)
):

    return create_webhook(
        db,
        data
    )



@router.get("/webhooks")
def list_webhooks(
    db: Session = Depends(get_db)
):

    return get_webhooks(
        db
    )



@router.put("/webhooks/{webhook_id}")
def edit_webhook(
    webhook_id: int,
    data: NotificationWebhookUpdate,
    db: Session = Depends(get_db)
):

    return update_webhook(
        db,
        webhook_id,
        data
    )



@router.delete("/webhooks/{webhook_id}")
def remove_webhook(
    webhook_id: int,
    db: Session = Depends(get_db)
):

    return delete_webhook(
        db,
        webhook_id
    )