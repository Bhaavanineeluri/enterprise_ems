from repositories.base import BaseRepository
from models.goods_receipt import GoodsReceipt


class GoodsReceiptRepository(BaseRepository[GoodsReceipt]):

    def __init__(self):
        super().__init__(GoodsReceipt)


goods_receipt_repository = GoodsReceiptRepository()