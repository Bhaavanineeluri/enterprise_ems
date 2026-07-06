from fastapi import Depends, HTTPException, status

from core.roles import Role
from dependencies.auth import get_current_user
from models.user import User


def require_roles(*allowed_roles: Role):
    """
    Usage:
        current_user: User = Depends(require_roles(Role.ADMIN))

        current_user: User = Depends(
            require_roles(Role.ADMIN, Role.MANAGER)
        )
    """

    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in [role.value for role in allowed_roles]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to perform this action."
            )
        return current_user

    return role_checker