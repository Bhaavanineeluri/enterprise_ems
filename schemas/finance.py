from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from datetime import date
from typing import Optional
from pydantic import BaseModel
from datetime import date
from typing import Optional


class GeneralLedgerCreate(BaseModel):

    account_code: str
    account_name: str
    account_type: str

    opening_balance: float = 0

    description: Optional[str] = None

    company_id: int


class GeneralLedgerUpdate(BaseModel):

    account_name: Optional[str] = None

    account_type: Optional[str] = None

    description: Optional[str] = None

    current_balance: Optional[float] = None

    is_active: Optional[bool] = None


class GeneralLedgerResponse(BaseModel):

    id: int

    account_code: str

    account_name: str

    account_type: str

    opening_balance: float

    current_balance: float

    description: Optional[str]

    company_id: int

    is_active: bool

    created_at: datetime

    class Config:
        from_attributes = True


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