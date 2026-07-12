from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.notification import (
    NotificationCreate,
    NotificationTemplateCreate,
    NotificationTemplateUpdate
)

from schemas.notification_webhook import (
    NotificationWebhookCreate,
    NotificationWebhookUpdate
)

from services.notification import (
    send_notification,
    get_notifications,
    create_template,
    get_templates,
    update_template,
    delete_template,
    create_webhook,
    get_webhooks,
    update_webhook,
    delete_webhook
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# =====================================================
# SEND NOTIFICATION
# =====================================================

@router.post(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "create"))
    ]
)
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

@router.get(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "view"))
    ]
)
def list_notifications(
    db: Session = Depends(get_db)
):
    return get_notifications(db)


# =====================================================
# CREATE TEMPLATE
# =====================================================

@router.post(
    "/templates",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "create"))
    ]
)
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

@router.get(
    "/templates",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "view"))
    ]
)
def list_templates(
    db: Session = Depends(get_db)
):
    return get_templates(db)


@router.put(
    "/templates/{template_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "update"))
    ]
)
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


@router.delete(
    "/templates/{template_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "delete"))
    ]
)
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

@router.post(
    "/webhooks",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "create"))
    ]
)
def add_webhook(
    data: NotificationWebhookCreate,
    db: Session = Depends(get_db)
):
    return create_webhook(
        db,
        data
    )


@router.get(
    "/webhooks",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "view"))
    ]
)
def list_webhooks(
    db: Session = Depends(get_db)
):
    return get_webhooks(db)


@router.put(
    "/webhooks/{webhook_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "update"))
    ]
)
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


@router.delete(
    "/webhooks/{webhook_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("notification", "delete"))
    ]
)
def remove_webhook(
    webhook_id: int,
    db: Session = Depends(get_db)
):
    return delete_webhook(
        db,
        webhook_id
    )