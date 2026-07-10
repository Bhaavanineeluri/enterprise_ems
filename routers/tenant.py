from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.tenant import TenantCreate

from services.tenant import (
    create_tenant,
    get_tenants
)


router = APIRouter(
    prefix="/tenants",
    tags=["Tenant"]
)


@router.post("/")
def create(
    data: TenantCreate,
    db: Session = Depends(get_db)
):

    return create_tenant(
        db,
        data
    )



@router.get("/")
def get_all(
    db: Session = Depends(get_db)
):

    return get_tenants(db)