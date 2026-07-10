from sqlalchemy.orm import Session

from models.tenant import Tenant


def create_tenant(
    db: Session,
    data
):

    tenant = Tenant(
        tenant_name=data.tenant_name,
        tenant_code=data.tenant_code
    )

    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    return tenant



def get_tenants(
    db: Session
):

    return db.query(Tenant).all()