from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from dependencies.roles import require_roles
from core.roles import Role
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_assignment import UserAssignment
from services.user_assignment import assign_user
from services.user import (
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
# Profile
# -----------------------------
@router.get(
    "/profile",
    response_model=UserResponse
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
    response_model=list[UserResponse]
)
def all_users(
    _=Depends(require_roles(
        Role.ADMIN,
        Role.MANAGER,
        Role.SUPER_ADMIN
    ))
):
    return get_all_users()


# -----------------------------
# Update Role
# -----------------------------
@router.put(
    "/role/{user_id}"
)
def change_role(
    user_id: int,
    role_data: UserRoleUpdate,
    _=Depends(require_roles(Role.SUPER_ADMIN))
):
    return update_user_role(user_id, role_data)


# -----------------------------
# Delete User
# -----------------------------
@router.delete(
    "/{user_id}"
)
def remove_user(
    user_id: int,
    _=Depends(require_roles(Role.SUPER_ADMIN))
):
    return delete_user(user_id)


router = APIRouter(prefix="/assign", tags=["User Assignment"])


@router.post("/")
def assign(data: UserAssignment, db: Session = Depends(get_db)):
    return assign_user(
        db,
        user_id=data.user_id,
        company_id=data.company_id,
        branch_id=data.branch_id,
        department_id=data.department_id,
        team_id=data.team_id
    )