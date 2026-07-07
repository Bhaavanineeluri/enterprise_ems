from repositories.base import BaseRepository
from models.purchase_request import PurchaseRequest


class PurchaseRequestRepository(BaseRepository[PurchaseRequest]):

    def __init__(self):
        super().__init__(PurchaseRequest)


purchase_request_repository = PurchaseRequestRepository()