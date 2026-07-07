from pydantic import BaseModel, ConfigDict


class NotificationCreate(BaseModel):

    user_id: int
    channel: str
    message: str
    template_id: int | None = None



class NotificationResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int
    user_id: int
    channel: str
    message: str
    status: str
    
class NotificationTemplateCreate(BaseModel):
    
    name: str
    channel: str
    subject: str | None = None
    message: str