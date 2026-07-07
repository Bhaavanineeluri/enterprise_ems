from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


# =====================================================
# INVOICE SCHEMAS
# =====================================================

class InvoiceCreate(BaseModel):
    invoice_number: str
    sales_order_id: int
    customer_id: int
    total_amount: float


class InvoiceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    invoice_number: str
    sales_order_id: int
    customer_id: int
    total_amount: float
    payment_status: str
    invoice_status: str
    created_at: datetime


# =====================================================
# PAYMENT SCHEMAS
# =====================================================

class PaymentCreate(BaseModel):
    payment_number: str
    invoice_id: int
    customer_id: int
    amount: float
    payment_method: str


class PaymentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    payment_number: str
    invoice_id: int
    customer_id: int
    amount: float
    payment_method: str
    payment_status: str
    created_at: datetime


# =====================================================
# TRANSACTION SCHEMAS
# =====================================================

class TransactionCreate(BaseModel):
    transaction_number: str
    payment_id: int
    amount: float
    transaction_type: str
    reference: Optional[str] = None


class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    transaction_number: str
    payment_id: int
    amount: float
    transaction_type: str
    reference: Optional[str] = None
    status: str
    created_at: datetime


# =====================================================
# JOURNAL ENTRY SCHEMAS
# =====================================================

class JournalEntryCreate(BaseModel):
    journal_number: str
    transaction_id: int
    account_name: str
    debit: float = 0
    credit: float = 0
    description: Optional[str] = None


class JournalEntryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    journal_number: str
    transaction_id: int
    account_name: str
    debit: float
    credit: float
    description: Optional[str] = None
    created_at: datetime


# =====================================================
# LEDGER SCHEMAS
# =====================================================

class LedgerCreate(BaseModel):
    ledger_name: str
    account_type: str
    opening_balance: float = 0
    description: Optional[str] = None


class LedgerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ledger_name: str
    account_type: str
    opening_balance: float
    current_balance: float
    description: Optional[str] = None
    created_at: datetime