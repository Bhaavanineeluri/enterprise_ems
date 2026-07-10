from pydantic import BaseModel
from datetime import date
from typing import Optional


class AccountsPayableCreate(BaseModel):

    vendor_id: int

    bill_number: str

    amount: float

    due_date: Optional[date] = None

    company_id: int



class AccountsPayableUpdate(BaseModel):

    paid_amount: Optional[float] = None

    status: Optional[str] = None



class AccountsPayableResponse(BaseModel):

    id: int

    vendor_id: int

    bill_number: str

    amount: float

    paid_amount: float

    due_date: Optional[date]

    status: str

    company_id: int


    class Config:
        from_attributes = True