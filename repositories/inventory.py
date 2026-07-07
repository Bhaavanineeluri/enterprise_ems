from repositories.base import BaseRepository
from models.inventory import Inventory


class InventoryRepository(BaseRepository[Inventory]):

    def __init__(self):
        super().__init__(Inventory)


inventory_repository = InventoryRepository()