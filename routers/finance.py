from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.finance import (
    InvoiceCreate,
    PaymentCreate,
    TransactionCreate,
    LedgerCreate
)

from services.finance import (
    create_invoice,
    get_invoices,
    get_invoice,

    create_payment,
    get_payments,

    create_transaction,
    get_transactions,

    create_ledger,
    get_ledgers
)


router = APIRouter(
    prefix="/finance",
    tags=["Finance"]
)



# =====================================================
# INVOICE
# =====================================================

@router.post("/invoices")
def add_invoice(
    data: InvoiceCreate,
    db: Session = Depends(get_db)
):

    return create_invoice(
        db,
        data
    )



@router.get("/invoices")
def list_invoices(
    db: Session = Depends(get_db)
):

    return get_invoices(db)



@router.get("/invoices/{invoice_id}")
def fetch_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):

    return get_invoice(
        db,
        invoice_id
    )




# =====================================================
# PAYMENT
# =====================================================

@router.post("/payments")
def add_payment(
    data: PaymentCreate,
    db: Session = Depends(get_db)
):

    return create_payment(
        db,
        data
    )



@router.get("/payments")
def list_payments(
    db: Session = Depends(get_db)
):

    return get_payments(db)




# =====================================================
# TRANSACTION
# =====================================================

@router.post("/transactions")
def add_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db)
):

    return create_transaction(
        db,
        data
    )



@router.get("/transactions")
def list_transactions(
    db: Session = Depends(get_db)
):

    return get_transactions(db)




# =====================================================
# LEDGER
# =====================================================

@router.post("/ledgers")
def add_ledger(
    data: LedgerCreate,
    db: Session = Depends(get_db)
):

    return create_ledger(
        db,
        data
    )



@router.get("/ledgers")
def list_ledgers(
    db: Session = Depends(get_db)
):

    return get_ledgers(db)