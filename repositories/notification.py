from sqlalchemy.orm import Session

from models.notification import Notification
from models.notification_template import NotificationTemplate



class NotificationRepository:


    def create(
        self,
        db: Session,
        notification: Notification
    ):

        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification



    def get_all(
        self,
        db: Session
    ):

        return db.query(Notification).all()



    def get(
        self,
        db: Session,
        notification_id: int
    ):

        return db.query(Notification).filter(
            Notification.id == notification_id
        ).first()



    def create_template(
        self,
        db: Session,
        template: NotificationTemplate
    ):

        db.add(template)
        db.commit()
        db.refresh(template)

        return template



    def get_templates(
        self,
        db: Session
    ):

        return db.query(NotificationTemplate).all()



notification_repository = NotificationRepository()