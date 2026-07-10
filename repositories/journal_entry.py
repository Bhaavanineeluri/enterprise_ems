from repositories.base import BaseRepository

from models.journal_entry import JournalEntry


JournalEntry_repository = BaseRepository(
    JournalEntry
)