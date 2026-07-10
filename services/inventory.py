from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork
from models.stock_adjustment import StockAdjustment


# =====================================================
# ADD / UPDATE INVENTORY
# =====================================================

def add_or_update_inventory(
    db: Session,
    data
):
    uow = UnitOfWork(db)

    product = uow.products.get(
        db,
        data.product_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    inventory = uow.inventory.first_by(
        db,
        product_id=data.product_id
    )

    if inventory:
        inventory.quantity = data.quantity
    else:
        inventory = uow.inventory.model(
            product_id=data.product_id,
            quantity=data.quantity
        )

        uow.inventory.create(
            db,
            inventory
        )

    try:
        uow.commit()
        uow.refresh(inventory)
        return inventory

    except Exception as e:
        uow.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Inventory update failed: {str(e)}"
        )


# =====================================================
# GET ALL INVENTORY
# =====================================================

def get_inventory(
    db: Session
):
    uow = UnitOfWork(db)

    return uow.inventory.get_all(db)


# =====================================================
# GET INVENTORY BY PRODUCT
# =====================================================

def get_inventory_by_product(
    db: Session,
    product_id: int
):
    uow = UnitOfWork(db)

    inventory = uow.inventory.first_by(
        db,
        product_id=product_id
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    return inventory


# =====================================================
# STOCK ADJUSTMENT
# =====================================================

def stock_adjustment(
    db: Session,
    data
):
    uow = UnitOfWork(db)

    inventory = uow.inventory.get(
        db,
        data.inventory_id
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    if data.adjustment_type == "IN":
        inventory.quantity += data.quantity

    elif data.adjustment_type == "OUT":

        if inventory.quantity < data.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        inventory.quantity -= data.quantity

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid adjustment type"
        )

    adjustment = StockAdjustment(
        inventory_id=data.inventory_id,
        adjustment_type=data.adjustment_type,
        quantity=data.quantity,
        reason=data.reason,
        created_by=data.created_by
    )

    db.add(adjustment)

    try:
        uow.commit()
        uow.refresh(inventory)

        return {
            "message": "Stock adjusted successfully",
            "current_quantity": inventory.quantity,
            "adjustment": adjustment
        }

    except Exception as e:
        uow.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Stock adjustment failed: {str(e)}"
        )


# =====================================================
# STOCK ADJUSTMENT HISTORY
# =====================================================

def stock_adjustment_history(
    db: Session,
    inventory_id: int
):
    return (
        db.query(StockAdjustment)
        .filter(
            StockAdjustment.inventory_id == inventory_id
        )
        .order_by(
            StockAdjustment.created_at.desc()
        )
        .all()
    )


# =====================================================
# OUT OF STOCK INVENTORY
# =====================================================

def out_of_stock_inventory(
    db: Session
):
    uow = UnitOfWork(db)

    return (
        db.query(uow.inventory.model)
        .filter(
            uow.inventory.model.quantity == 0
        )
        .all()
    )


# =====================================================
# LOW STOCK INVENTORY
# =====================================================

def low_stock_inventory(
    db: Session,
    threshold: int = 10
):
    uow = UnitOfWork(db)

    return (
        db.query(uow.inventory.model)
        .filter(
            uow.inventory.model.quantity <= threshold
        )
        .all()
    )