from repositories.base import BaseRepository
from models.vendor import Vendor


class VendorRepository(BaseRepository[Vendor]):

    def __init__(self):
        super().__init__(Vendor)


vendor_repository = VendorRepository()