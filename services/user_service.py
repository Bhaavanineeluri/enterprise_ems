from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRoleUpdate


# ----------------------------------------
# Database Session
# ----------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------------------
# Logged-in User Profile
# ----------------------------------------
def get_my_profile(current_user: User):
    return current_user


# ----------------------------------------
# Get All Users
# ----------------------------------------
def get_all_users():
    db: Session = SessionLocal()

    try:
        users = db.query(User).all()
        return users

    finally:
        db.close()


# ----------------------------------------
# Update User Role
# ----------------------------------------
def update_user_role(user_id: int, role_data: UserRoleUpdate):
    db: Session = SessionLocal()

    try:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        user.role = role_data.role

        db.commit()
        db.refresh(user)

        return {
            "message": "User role updated successfully",
            "user_id": user.id,
            "role": user.role
        }

    finally:
        db.close()


# ----------------------------------------
# Delete User
# ----------------------------------------
def delete_user(user_id: int):
    db: Session = SessionLocal()

    try:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        db.delete(user)
        db.commit()

        return {
            "message": "User deleted successfully"
        }

    finally:
        db.close()