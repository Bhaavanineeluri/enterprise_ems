from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.vendor import VendorCreate, VendorResponse
from services.vendor import create_vendor, get_vendors

router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post("/", response_model=VendorResponse)
def create(data: VendorCreate, db: Session = Depends(get_db)):
    return create_vendor(db, data)


@router.get("/", response_model=list[VendorResponse])
def list_all(db: Session = Depends(get_db)):
    return get_vendors(db)