from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.notification import (
    NotificationCreate,
    NotificationTemplateCreate
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