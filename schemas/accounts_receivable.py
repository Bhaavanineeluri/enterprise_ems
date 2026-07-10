from pydantic import BaseModel
from datetime import date
from typing import Optional



class AccountsReceivableCreate(BaseModel):

    customer_id: int

    invoice_number: str

    amount: float

    due_date: Optional[date] = None

    company_id: int



class AccountsReceivableUpdate(BaseModel):

    received_amount: Optional[float] = None

    status: Optional[str] = None



class AccountsReceivableResponse(BaseModel):

    id: int

    customer_id: int

    invoice_number: str

    amount: float

    received_amount: float

    due_date: Optional[date]

    status: str

    company_id: int


    class Config:
        from_attributes = True