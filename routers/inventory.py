from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.inventory import InventoryUpdate, InventoryResponse
from services.inventory import add_or_update_inventory, get_inventory

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/", response_model=InventoryResponse)
def update(data: InventoryUpdate, db: Session = Depends(get_db)):
    return add_or_update_inventory(db, data)


@router.get("/", response_model=list[InventoryResponse])
def list_all(db: Session = Depends(get_db)):
    return get_inventory(db)