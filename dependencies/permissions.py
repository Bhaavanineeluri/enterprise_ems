from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.user import User
from models.role import Role
from models.role_permission import RolePermission
from models.resource import Resource
from models.permission import Permission

from dependencies.auth import get_current_user



def require_permission(
    resource_name: str,
    action_name: str
):

    def checker(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):


        role = db.query(Role).filter(
            Role.name == current_user.role
        ).first()


        if not role:

            raise HTTPException(
                status_code=403,
                detail="Role not found"
            )


        permission = (
            db.query(RolePermission)
            .join(Resource)
            .join(Permission)
            .filter(
                RolePermission.role_id == role.id,
                Resource.name == resource_name,
                Permission.action == action_name
            )
            .first()
        )


        if not permission:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )


        return current_user


    return checker