from fastapi import HTTPException, Request
from sqlalchemy.orm import Session

from models.user import User
from models.customer import Customer
from models.employee import Employee

from schemas.user import (
    ForgotPasswordRequest,
    ResetPasswordRequest,
    UserRegister,
    UserRole
)

from core.unit_of_work.uow import UnitOfWork

from services.otp import create_otp, verify_otp

from utils.password import hash_password, verify_password

from repositories.user import user_repository



# =====================================================
# REGISTER USER
# =====================================================

def register_user(
    user: UserRegister,
    db: Session
):

    uow = UnitOfWork(db)


    allowed_roles = [
        role.value
        for role in UserRole
    ]


    if user.role.value not in allowed_roles:

        raise HTTPException(
            status_code=400,
            detail="Invalid role"
        )



    # Duplicate check

    if uow.users.exists(
        db,
        email=user.email
    ):

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    if uow.users.exists(
        db,
        phone=user.phone
    ):

        raise HTTPException(
            status_code=400,
            detail="Phone already exists"
        )



    try:

        # Create User

        new_user = User(

            full_name=user.full_name,

            email=user.email,

            phone=user.phone,

            password=hash_password(
                user.password
            ),

            role=user.role.value,

            mfa_enabled=False
        )


        uow.users.create(
            db,
            new_user
        )


        # Need user id

        uow.flush()



        # Create profile

        if user.role == UserRole.CUSTOMER:

            customer = Customer(
                user_id=new_user.id
            )

            uow.customers.create(
                db,
                customer
            )



        elif user.role in [
            UserRole.EMPLOYEE,
            UserRole.MANAGER
        ]:


            employee = Employee(

                user_id=new_user.id,

                designation=(
                    "Manager"
                    if user.role == UserRole.MANAGER
                    else "Employee"
                )
            )


            uow.employees.create(
                db,
                employee
            )



        # Single transaction commit

        uow.commit()

        uow.refresh(
            new_user
        )


        return new_user



    except Exception as e:

        uow.rollback()

        raise HTTPException(

            status_code=500,

            detail=f"Registration failed: {str(e)}"

        )





# =====================================================
# LOGIN USER
# =====================================================

def login_user(
    login_data,
    db: Session,
    request: Request
):

    ip_address = (
        request.headers.get("x-forwarded-for")
        or request.client.host
    )



    db_user = user_repository.first_by(
        db,
        email=login_data.email
    )


    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )



    if not verify_password(
        login_data.password,
        db_user.password
    ):

        


        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
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





# =====================================================
# FORGOT PASSWORD
# =====================================================

def forgot_password(
    data: ForgotPasswordRequest,
    db: Session
):

    user = user_repository.first_by(
        db,
        email=data.email
    )


    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    otp = create_otp(
        db=db,
        user_id=user.id,
        purpose="FORGOT_PASSWORD"
    )


    return {

        "message": "OTP generated successfully",

        "otp": otp

    }





# =====================================================
# RESET PASSWORD
# =====================================================

def reset_password(
    data: ResetPasswordRequest,
    db: Session
):

    user = user_repository.first_by(
        db,
        email=data.email
    )


    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



    valid, message = verify_otp(

        db=db,

        user_id=user.id,

        otp=data.otp,

        purpose="FORGOT_PASSWORD"

    )


    if not valid:

        raise HTTPException(
            status_code=400,
            detail=message
        )



    try:

        user.password = hash_password(
            data.new_password
        )


        db.commit()


        return {

            "message":
            "Password reset successful"

        }



    except Exception as e:

        db.rollback()


        raise HTTPException(

            status_code=500,

            detail=f"Reset failed: {str(e)}"

        )