from urllib import request

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schemas.mfa import MFAResponse
from services.token import generate_tokens
from models.user import User
from services.token import logout
from services.otp import  verify_otp
from schemas.user import (
    ForgotPasswordRequest,
    ResetPasswordRequest
)
from fastapi import Request
from services.auth import (
    forgot_password,
    reset_password
)
from schemas.user import (
    UserRegister,
    UserResponse,
    UserLogin,
    Token,
)


from services.auth import (
    register_user,
    login_user,
)





router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    description="Register a new user. Choose role as admin, employee, or customer."
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(user, db)


@router.post(
    "/login",
    response_model=MFAResponse,
    description="Login using email and password. If credentials are valid, an OTP will be sent."
)
def login(
    user: UserLogin,
    request: Request,
    db: Session = Depends(get_db)
):
    return login_user(user, db,request)


@router.post(
    "/verify-otp-login",
    response_model=Token
)
def verify_login_otp(
    user_id: int,
    otp: str,
    db: Session = Depends(get_db)
):

    valid, message = verify_otp(
        db=db,
        user_id=user_id,
        otp=otp,
        purpose="LOGIN"
    )

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return generate_tokens(user)

@router.post("/forgot-password")
def forgot_password_api(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    return forgot_password(request, db)

@router.post("/reset-password")
def reset_password_api(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return reset_password(request, db)

@router.post("/logout")
def logout_user():
    return logout()