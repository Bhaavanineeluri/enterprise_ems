from pydantic import BaseModel, ConfigDict


class UserPreferenceUpdate(BaseModel):

    theme: str | None = None
    language: str | None = None
    timezone: str | None = None
    date_format: str | None = None

    email_notifications: bool | None = None
    sms_notifications: bool | None = None
    push_notifications: bool | None = None


class UserPreferenceResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    user_id: int

    theme: str
    language: str
    timezone: str
    date_format: str

    email_notifications: bool
    sms_notifications: bool
    push_notifications: bool