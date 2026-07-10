from sqlalchemy.orm import Session

from models.journal_entry import JournalEntry
from repositories.journal_entry import journal_entry_repository


def create_journal_entry(
    db: Session,
    data
):

    journal = JournalEntry(
        **data.model_dump()
    )

    return journal_entry_repository.create(
        db,
        journal
    )


def get_journal_entries(
    db: Session
):

    return journal_entry_repository.get_all(db)


def get_journal_entry(
    db: Session,
    journal_id: int
):

    return journal_entry_repository.get(
        db,
        journal_id
    )