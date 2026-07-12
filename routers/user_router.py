from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.user import (
    UserResponse,
    UserRoleUpdate
)

from schemas.user_preference import (
    UserPreferenceUpdate,
    UserPreferenceResponse
)

from services.user import (
    get_my_profile,
    get_all_users,
    update_user_role,
    delete_user
)

from services.user_preference import (
    get_my_preferences,
    update_my_preferences
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -----------------------------
# Profile
# -----------------------------
@router.get(
    "/profile",
    response_model=UserResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("user", "view"))
    ]
)
def profile(
    current_user=Depends(get_current_user)
):
    return get_my_profile(current_user)


# -----------------------------
# Get All Users
# -----------------------------
@router.get(
    "/all",
    response_model=list[UserResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("user", "view"))
    ]
)
def all_users():
    return get_all_users()


# -----------------------------
# Update Role
# -----------------------------
@router.put(
    "/role/{user_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("user", "update_role"))
    ]
)
def change_role(
    user_id: int,
    role_data: UserRoleUpdate
):
    return update_user_role(
        user_id,
        role_data
    )


# -----------------------------
# Delete User
# -----------------------------
@router.delete(
    "/{user_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("user", "delete"))
    ]
)
def remove_user(
    user_id: int
):
    return delete_user(user_id)


# -----------------------------
# My Preferences
# -----------------------------
@router.get(
    "/me/preferences",
    response_model=UserPreferenceResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("user_preference", "view"))
    ]
)
def my_preferences(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_my_preferences(
        db,
        current_user
    )


# -----------------------------
# Update My Preferences
# -----------------------------
@router.put(
    "/me/preferences",
    response_model=UserPreferenceResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("user_preference", "update"))
    ]
)
def update_preferences(
    data: UserPreferenceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_my_preferences(
        db,
        current_user,
        data
    )