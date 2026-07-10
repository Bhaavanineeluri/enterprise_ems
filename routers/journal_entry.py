from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.journal_entry import (
    JournalEntryCreate,
    JournalEntryResponse
)

from services.journal_entry import (
    create_journal_entry,
    get_journal_entries,
    get_journal_entry
)

router = APIRouter(
    prefix="/journal-entries",
    tags=["Journal Entries"]
)


@router.post(
    "/",
    response_model=JournalEntryResponse
)
def create(
    data: JournalEntryCreate,
    db: Session = Depends(get_db)
):
    return create_journal_entry(db, data)


@router.get("/")
def list_entries(
    db: Session = Depends(get_db)
):
    return get_journal_entries(db)


@router.get("/{journal_id}")
def get(
    journal_id: int,
    db: Session = Depends(get_db)
):
    return get_journal_entry(db, journal_id)