from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.goods_receipt import (
    GoodsReceiptCreate,
    GoodsReceiptResponse
)

from services.goods_receipt import (
    create_goods_receipt,
    get_goods_receipts
)

router = APIRouter(
    prefix="/goods-receipts",
    tags=["Goods Receipt"]
)


@router.post("/", response_model=GoodsReceiptResponse)
def create(
    data: GoodsReceiptCreate,
    db: Session = Depends(get_db)
):
    return create_goods_receipt(db, data)


@router.get("/", response_model=list[GoodsReceiptResponse])
def get_all(db: Session = Depends(get_db)):
    return get_goods_receipts(db)


@router.get("/{receipt_id}", response_model=GoodsReceiptResponse)
def get_one(
    receipt_id: int,
    db: Session = Depends(get_db)
):
    return get_goods_receipts(db, receipt_id)