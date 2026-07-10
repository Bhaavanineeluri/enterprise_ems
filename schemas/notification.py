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
    
from pydantic import BaseModel, ConfigDict
from typing import Optional



class NotificationTemplateUpdate(BaseModel):

    subject: Optional[str] = None

    message: Optional[str] = None

    is_active: Optional[bool] = None



class NotificationTemplateResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int

    name: str

    channel: str

    subject: Optional[str]

    message: str

    is_active: bool