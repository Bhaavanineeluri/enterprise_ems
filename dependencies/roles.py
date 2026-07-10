from fastapi import Depends, HTTPException, status

from dependencies.auth import get_current_user


def require_roles(*roles):

    def checker(
        current_user=Depends(get_current_user)
    ):

        user_role = current_user.role

        if user_role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )

        return current_user

    return checker