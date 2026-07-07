from repositories.base import BaseRepository
from models.purchase_order import PurchaseOrder


class PurchaseOrderRepository(BaseRepository[PurchaseOrder]):

    def __init__(self):
        super().__init__(PurchaseOrder)


purchase_order_repository = PurchaseOrderRepository()