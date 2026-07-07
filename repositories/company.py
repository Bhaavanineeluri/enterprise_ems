from repositories.base import BaseRepository
from models.company import Company


class CompanyRepository(BaseRepository[Company]):

    def __init__(self):
        super().__init__(Company)


company_repository = CompanyRepository()