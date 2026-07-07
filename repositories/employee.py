from repositories.base import BaseRepository
from models.employee import Employee


class EmployeeRepository(BaseRepository[Employee]):

    def __init__(self):
        super().__init__(Employee)


employee_repository = EmployeeRepository()