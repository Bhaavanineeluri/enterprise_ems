from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from core.roles import Role
class UserRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"
    MANAGER ="manager"
    CUSTOMER = "customer"

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str
    role: UserRole = Field(
        description="choose one : admin, employee,customer."
    )
    


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    role: UserRole
    is_active: bool
    is_verified: bool

    class Config:
        from_attributes = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    
class RefreshTokenRequest(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str



class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    otp: str
    new_password: str
    
class UserRoleUpdate(BaseModel):
    role: Role

