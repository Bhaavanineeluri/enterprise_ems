from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.goods_receipt import (
    GoodsReceiptCreate,
    GoodsReceiptResponse
)

from services.goods_receipt import (
    create_goods_receipt,
    get_goods_receipts,
    get_goods_receipt
)

router = APIRouter(
    prefix="/goods-receipts",
    tags=["Goods Receipt"]
)


@router.post(
    "/",
    response_model=GoodsReceiptResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("goods_receipt", "create"))
    ]
)
def create(
    data: GoodsReceiptCreate,
    db: Session = Depends(get_db)
):
    return create_goods_receipt(db, data)


@router.get(
    "/",
    response_model=list[GoodsReceiptResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("goods_receipt", "view"))
    ]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_goods_receipts(db)


@router.get(
    "/{receipt_id}",
    response_model=GoodsReceiptResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("goods_receipt", "view"))
    ]
)
def get_one(
    receipt_id: int,
    db: Session = Depends(get_db)
):
    return get_goods_receipt(db, receipt_id)