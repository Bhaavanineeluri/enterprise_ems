from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.inventory import (
    InventoryUpdate,
    InventoryResponse,
    StockAdjustmentRequest,
    StockAdjustmentResponse
)

from services.inventory import (
    add_or_update_inventory,
    get_inventory,
    stock_adjustment,
    get_inventory_by_product,
    low_stock_inventory,
    out_of_stock_inventory,
    stock_adjustment_history
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


# =====================================================
# CREATE / UPDATE INVENTORY
# =====================================================

@router.post(
    "/",
    response_model=InventoryResponse
)
def update(
    data: InventoryUpdate,
    db: Session = Depends(get_db)
):
    return add_or_update_inventory(
        db,
        data
    )


# =====================================================
# GET ALL INVENTORY
# =====================================================

@router.get(
    "/",
    response_model=list[InventoryResponse]
)
def list_all(
    db: Session = Depends(get_db)
):
    return get_inventory(db)


# =====================================================
# STOCK ADJUSTMENT
# =====================================================

@router.post(
    "/stock-adjustment",
    response_model=StockAdjustmentResponse
)
def adjust_stock(
    data: StockAdjustmentRequest,
    db: Session = Depends(get_db)
):
    return stock_adjustment(
        db,
        data
    )


# =====================================================
# GET INVENTORY BY PRODUCT
# =====================================================

@router.get(
    "/product/{product_id}",
    response_model=InventoryResponse
)
def inventory_by_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_inventory_by_product(
        db,
        product_id
    )


# =====================================================
# LOW STOCK
# =====================================================

@router.get(
    "/low-stock",
    response_model=list[InventoryResponse]
)
def low_stock(
    threshold: int = 10,
    db: Session = Depends(get_db)
):
    return low_stock_inventory(
        db,
        threshold
    )


# =====================================================
# OUT OF STOCK
# =====================================================

@router.get(
    "/out-of-stock",
    response_model=list[InventoryResponse]
)
def out_of_stock(
    db: Session = Depends(get_db)
):
    return out_of_stock_inventory(db)


# =====================================================
# STOCK HISTORY
# =====================================================

@router.get(
    "/history/{inventory_id}"
)
def adjustment_history(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return stock_adjustment_history(
        db,
        inventory_id
    )