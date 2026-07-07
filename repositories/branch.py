from repositories.base import BaseRepository
from models.branch import Branch


class BranchRepository(BaseRepository[Branch]):

    def __init__(self):
        super().__init__(Branch)


branch_repository = BranchRepository()