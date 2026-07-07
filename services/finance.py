from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.invoice import Invoice
from models.payment import Payment
from models.transaction import Transaction
from models.ledger import Ledger

from schemas.finance import (
    InvoiceCreate,
    PaymentCreate,
    TransactionCreate,
    LedgerCreate
)

from core.unit_of_work import UnitOfWork



# =====================================================
# INVOICE
# =====================================================

def create_invoice(
    db: Session,
    data: InvoiceCreate
):

    uow = UnitOfWork(db)


    existing = db.query(Invoice).filter(
        Invoice.invoice_number == data.invoice_number
    ).first()


    if existing:
        raise HTTPException(
            status_code=400,
            detail="Invoice already exists"
        )


    invoice = Invoice(
        invoice_number=data.invoice_number,
        sales_order_id=data.sales_order_id,
        customer_id=data.customer_id,
        total_amount=data.total_amount
    )


    uow.invoices.create(
        db,
        invoice
    )


    db.commit()
    db.refresh(invoice)


    return invoice




def get_invoices(
    db: Session
):

    uow = UnitOfWork(db)

    return uow.invoices.get_all(db)



def get_invoice(
    db: Session,
    invoice_id: int
):

    uow = UnitOfWork(db)


    invoice = uow.invoices.get(
        db,
        invoice_id
    )


    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )


    return invoice





# =====================================================
# PAYMENT
# =====================================================

def create_payment(
    db: Session,
    data: PaymentCreate
):

    uow = UnitOfWork(db)


    existing = db.query(Payment).filter(
        Payment.payment_number == data.payment_number
    ).first()


    if existing:
        raise HTTPException(
            status_code=400,
            detail="Payment already exists"
        )


    payment = Payment(
        payment_number=data.payment_number,
        invoice_id=data.invoice_id,
        customer_id=data.customer_id,
        amount=data.amount,
        payment_method=data.payment_method
    )


    uow.payments.create(
        db,
        payment
    )


    db.commit()
    db.refresh(payment)


    return payment




def get_payments(
    db: Session
):

    uow = UnitOfWork(db)

    return uow.payments.get_all(db)





# =====================================================
# TRANSACTION
# =====================================================

def create_transaction(
    db: Session,
    data: TransactionCreate
):

    uow = UnitOfWork(db)


    transaction = Transaction(
        transaction_number=data.transaction_number,
        payment_id=data.payment_id,
        amount=data.amount,
        transaction_type=data.transaction_type,
        reference=data.reference
    )


    uow.transactions.create(
        db,
        transaction
    )


    db.commit()
    db.refresh(transaction)


    return transaction





def get_transactions(
    db: Session
):

    uow = UnitOfWork(db)

    return uow.transactions.get_all(db)





# =====================================================
# LEDGER
# =====================================================

def create_ledger(
    db: Session,
    data: LedgerCreate
):

    uow = UnitOfWork(db)


    existing = db.query(Ledger).filter(
        Ledger.ledger_name == data.ledger_name
    ).first()


    if existing:
        raise HTTPException(
            status_code=400,
            detail="Ledger already exists"
        )


    ledger = Ledger(
        ledger_name=data.ledger_name,
        account_type=data.account_type,
        opening_balance=data.opening_balance,
        current_balance=data.opening_balance,
        description=data.description
    )


    uow.ledgers.create(
        db,
        ledger
    )


    db.commit()
    db.refresh(ledger)


    return ledger




def get_ledgers(
    db: Session
):

    uow = UnitOfWork(db)

    return uow.ledgers.get_all(db)