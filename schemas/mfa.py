from pydantic import BaseModel



class MFAResponse(BaseModel):
    mfa_required: bool
    message: str
    user_id: int
    otp: str