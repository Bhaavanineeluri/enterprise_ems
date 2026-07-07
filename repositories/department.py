from repositories.base import BaseRepository
from models.department import Department


class DepartmentRepository(BaseRepository[Department]):

    def __init__(self):
        super().__init__(Department)


department_repository = DepartmentRepository()