from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JournalEntryCreate(BaseModel):

    reference_no: str

    description: Optional[str] = None

    company_id: int

    created_by: int


class JournalEntryUpdate(BaseModel):

    description: Optional[str] = None


class JournalEntryResponse(BaseModel):

    id: int

    reference_no: str

    description: Optional[str]

    company_id: int

    created_by: int

    entry_date: datetime

    created_at: datetime

    class Config:
        from_attributes = True