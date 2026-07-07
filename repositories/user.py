from repositories.base import BaseRepository
from models.user import User


class UserRepository(BaseRepository[User]):

    def __init__(self):
        super().__init__(User)


user_repository = UserRepository()