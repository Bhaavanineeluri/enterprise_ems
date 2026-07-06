from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from database import get_db

from models.user import User

from schemas.user import (
    UserRegister,
    UserResponse,
    UserLogin,
    Token,
    ForgotPasswordRequest,
    ResetPasswordRequest,
)
from schemas.mfa import MFAResponse

from services.auth import (
    register_user,
    login_user,
    forgot_password,
    reset_password,
)
from services.otp import verify_otp
from services.token import generate_tokens, logout


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# ----------------------------------
# Register User
# ----------------------------------
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


# ----------------------------------
# Login (Password Verification + Send OTP)
# ----------------------------------
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
    return login_user(user, db, request)


# ----------------------------------
# Verify Login OTP
# ----------------------------------
@router.post(
    "/verify-otp-login",
    response_model=Token,
    description="Verify OTP and generate JWT access and refresh tokens."
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

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return generate_tokens(user)


# ----------------------------------
# Forgot Password
# ----------------------------------
@router.post("/forgot-password")
def forgot_password_api(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    return forgot_password(request, db)


# ----------------------------------
# Reset Password
# ----------------------------------
@router.post("/reset-password")
def reset_password_api(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return reset_password(request, db)


# ----------------------------------
# Logout
# ----------------------------------
@router.post("/logout")
def logout_user():
    return logout()