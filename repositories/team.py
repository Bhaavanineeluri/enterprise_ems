from repositories.base import BaseRepository
from models.team import Team


class TeamRepository(BaseRepository[Team]):

    def __init__(self):
        super().__init__(Team)


team_repository = TeamRepository()