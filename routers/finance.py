from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.finance import (
    GeneralLedgerCreate,
    GeneralLedgerResponse
)

from schemas.accounts_payable import (
    AccountsPayableCreate,
    AccountsPayableResponse
)

from schemas.accounts_receivable import (
    AccountsReceivableCreate,
    AccountsReceivableResponse
)

from services.finance import (
    trial_balance,
    profit_loss,
    balance_sheet
)
from services.finance import (
    create_ledger,
    get_ledgers,

    create_payable,
    get_payables,

    create_receivable,
    get_receivables
)


router = APIRouter(
    prefix="/finance",
    tags=["Finance & Accounting"]
)


# =====================================================
# GENERAL LEDGER
# =====================================================

@router.post(
    "/ledgers",
    response_model=GeneralLedgerResponse
)
def create_general_ledger(
    data: GeneralLedgerCreate,
    db: Session = Depends(get_db)
):

    return create_ledger(
        db,
        data
    )


@router.get(
    "/ledgers"
)
def list_ledgers(
    db: Session = Depends(get_db)
):

    return get_ledgers(db)



# =====================================================
# ACCOUNTS PAYABLE
# =====================================================


@router.post(
    "/accounts-payable",
    response_model=AccountsPayableResponse
)
def create_accounts_payable(
    data: AccountsPayableCreate,
    db: Session = Depends(get_db)
):

    return create_payable(
        db,
        data
    )


@router.get(
    "/accounts-payable"
)
def list_accounts_payable(
    db: Session = Depends(get_db)
):

    return get_payables(db)



# =====================================================
# ACCOUNTS RECEIVABLE
# =====================================================


@router.post(
    "/accounts-receivable",
    response_model=AccountsReceivableResponse
)
def create_accounts_receivable(
    data: AccountsReceivableCreate,
    db: Session = Depends(get_db)
):

    return create_receivable(
        db,
        data
    )


@router.get(
    "/accounts-receivable"
)
def list_accounts_receivable(
    db: Session = Depends(get_db)
):

    return get_receivables(db)

# =====================================================
# FINANCIAL REPORTS
# =====================================================


@router.get(
    "/reports/trial-balance"
)
def get_trial_balance(
    db: Session = Depends(get_db)
):

    return trial_balance(db)



@router.get(
    "/reports/profit-loss"
)
def get_profit_loss(
    db: Session = Depends(get_db)
):

    return profit_loss(db)



@router.get(
    "/reports/balance-sheet"
)
def get_balance_sheet(
    db: Session = Depends(get_db)
):

    return balance_sheet(db)