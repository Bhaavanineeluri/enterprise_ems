from ipaddress import ip_address

from fastapi import HTTPException, Request
from sqlalchemy.orm import Session


from models.employee import Employee
from models.customer import Customer

from models.user import User

from schemas.user import (
    ForgotPasswordRequest,
    ResetPasswordRequest,
    UserRegister,
    UserRole,
)

from services.login_history import create_login_history
from services.otp import create_otp, verify_otp
from services.token import generate_tokens

from utils.password import hash_password, verify_password
def register_user(user: UserRegister, db: Session):
    
    # -----------------------
    # VALIDATE ROLE
    # -----------------------
    allowed_roles = [role.value for role in UserRole]

    if user.role.value not in allowed_roles:
        raise HTTPException(
            status_code=400,
            detail="Role must be admin, employee, or customer."
        )

    # -----------------------
    # CHECK DUPLICATES
    # -----------------------
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    if db.query(User).filter(User.phone == user.phone).first():
        raise HTTPException(status_code=400, detail="Phone already exists")

    # -----------------------
    # CREATE USER
    # -----------------------
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hash_password(user.password),
        role=user.role,
        mfa_enabled=False
    )
    
    db.add(new_user)
    db.flush() 
    db.commit()
    db.refresh(new_user)
# ---------------------------------
# CREATE ROLE SPECIFIC PROFILE
# ---------------------------------
    if new_user.role == "customer":
        customer = Customer(user_id=new_user.id)
        db.add(customer)

    elif new_user.role == "employee":
        employee = Employee(
        user_id=new_user.id,
        designation="Employee"
    )
    db.add(employee)
        
    db.commit()
    

    
    return new_user



def login_user(login_data, db: Session, request: Request):

    ip_address = request.client.host

    db_user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    # User not found
    if not db_user:

        create_login_history(
            db=db,
            user_id=None,
            ip_address=ip_address,
            status="Failed"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Wrong password
    if not verify_password(
        login_data.password,
        db_user.password
    ):

        create_login_history(
            db=db,
            user_id=db_user.id,
            ip_address=ip_address,
            status="Failed"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Successful login
    create_login_history(
        db=db,
        user_id=db_user.id,
        ip_address=ip_address,
        status="Success"
    )

    otp = create_otp(
        db=db,
        user_id=db_user.id,
        purpose="LOGIN"
    )

    return {
        "mfa_required": True,
        "message": "OTP sent successfully",
        "user_id": db_user.id,
        "otp": otp
    } 
def forgot_password(data: ForgotPasswordRequest, db: Session):
    
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    otp = create_otp(
        db=db,
        user_id=user.id,
        purpose="forgot_password"
    )

    return {
        "message": "OTP generated successfully",
        "otp": otp
    }
    
def reset_password(data: ResetPasswordRequest, db: Session):
    
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    valid, message = verify_otp(
    db=db,
    user_id=user.id,
    otp=data.otp,
    purpose="forgot_password"
    )

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    user.password = hash_password(data.new_password)

    db.commit()
    
    return {
        "message": "Password reset successful"
    }