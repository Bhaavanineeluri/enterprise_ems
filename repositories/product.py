from repositories.base import BaseRepository
from models.product import Product


class ProductRepository(BaseRepository[Product]):

    def __init__(self):
        super().__init__(Product)


product_repository = ProductRepository()