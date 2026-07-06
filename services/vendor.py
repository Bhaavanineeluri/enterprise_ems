from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.vendor import Vendor


def create_vendor(db: Session, data):

    if db.query(Vendor).filter(Vendor.vendor_code == data.vendor_code).first():
        raise HTTPException(status_code=400, detail="Vendor exists")

    vendor = Vendor(**data.dict())

    db.add(vendor)
    db.commit()
    db.refresh(vendor)

    return vendor


def get_vendors(db: Session):
    return db.query(Vendor).all()