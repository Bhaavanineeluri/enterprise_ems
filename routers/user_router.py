from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from dependencies.permission import require_roles
from core.roles import Role

from models.user import User

from services.user_service import (
    get_my_profile,
    get_all_users,
    update_user_role,
    delete_user
)

from schemas.user import (
    UserResponse,
    UserRoleUpdate
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -----------------------------
# Logged-in User Profile
# -----------------------------
@router.get(
    "/profile",
    response_model=UserResponse
)
def profile(
    current_user: User = Depends(get_current_user)
):
    return get_my_profile(current_user)


# -----------------------------
# Get All Users
# -----------------------------
@router.get(
    "/all",
    response_model=list[UserResponse]
)
def all_users(
    current_user: User = Depends(
        require_roles(
            Role.ADMIN,
            Role.MANAGER,
            Role.SUPER_ADMIN
        )
    )
):
    return get_all_users()


# -----------------------------
# Update User Role
# -----------------------------
@router.put(
    "/role/{user_id}"
)
def change_role(
    user_id: int,
    role_data: UserRoleUpdate,
    current_user: User = Depends(
        require_roles(
            Role.SUPER_ADMIN
        )
    )
):
    return update_user_role(
        user_id,
        role_data
    )


# -----------------------------
# Delete User
# -----------------------------
@router.delete(
    "/{user_id}"
)
def remove_user(
    user_id: int,
    current_user: User = Depends(
        require_roles(
            Role.SUPER_ADMIN
        )
    )
):
    return delete_user(user_id)
from dependencies.auth import get_current_user
from dependencies.rbac import check_permission


@router.get("/all")
def get_users(
    current_user=Depends(get_current_user),
    _=Depends(check_permission("view_users"))
):
    return {"message": "You can view users"}