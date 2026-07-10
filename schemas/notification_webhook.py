from pydantic import BaseModel, ConfigDict
from typing import Optional


class NotificationWebhookCreate(BaseModel):

    event: str

    url: str



class NotificationWebhookUpdate(BaseModel):

    url: Optional[str] = None

    is_active: Optional[bool] = None



class NotificationWebhookResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int

    event: str

    url: str

    is_active: bool