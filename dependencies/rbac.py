from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.role_permission import RolePermission
from models.permission import Permission


def check_permission(permission_code: str):

    def wrapper(user: User, db: Session = Depends(get_db)):

        permission = db.query(Permission).filter(
            Permission.code == permission_code
        ).first()

        if not permission:
            raise HTTPException(status_code=404, detail="Permission not found")

        role_permissions = db.query(RolePermission).filter(
            RolePermission.role_id == user.role_id,
            RolePermission.permission_id == permission.id
        ).first()

        if not role_permissions:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return user

    return wrapper