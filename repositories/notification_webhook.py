from repositories.base import BaseRepository

from models.notification_webhook import NotificationWebhook


notification_webhook_repository = BaseRepository(
    NotificationWebhook
)