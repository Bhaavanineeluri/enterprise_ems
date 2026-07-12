from fastapi import HTTPException


def verify_company_access(current_user, resource):

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="Resource not found."
        )

    if current_user.role.name == "SUPER_ADMIN":
        return

    if getattr(resource, "company_id", None) != current_user.company_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied."
        )