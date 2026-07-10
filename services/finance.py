from sqlalchemy.orm import Session

from models.general_ledger import GeneralLedger
from models.accounts_payable import AccountsPayable
from models.accounts_receivable import AccountsReceivable


from repositories.general_ledger import (
    general_ledger_repository
)

from repositories.accounts_payable import (
    accounts_payable_repository
)

from repositories.accounts_receivable import (
    accounts_receivable_repository
)



# =====================================================
# GENERAL LEDGER
# =====================================================


def create_ledger(
    db: Session,
    data
):

    ledger = GeneralLedger(
        **data.model_dump()
    )

    return general_ledger_repository.create(
        db,
        ledger
    )


def get_ledgers(
    db: Session
):

    return general_ledger_repository.get_all(
        db
    )



# =====================================================
# ACCOUNTS PAYABLE
# =====================================================


def create_payable(
    db: Session,
    data
):

    payable = AccountsPayable(
        **data.model_dump()
    )

    return accounts_payable_repository.create(
        db,
        payable
    )


def get_payables(
    db: Session
):

    return accounts_payable_repository.get_all(
        db
    )



# =====================================================
# ACCOUNTS RECEIVABLE
# =====================================================


def create_receivable(
    db: Session,
    data
):

    receivable = AccountsReceivable(
        **data.model_dump()
    )


    return accounts_receivable_repository.create(
        db,
        receivable
    )


def get_receivables(
    db: Session
):

    return accounts_receivable_repository.get_all(
        db
    )
from models.general_ledger import GeneralLedger
from models.accounts_payable import AccountsPayable
from models.accounts_receivable import AccountsReceivable



# =====================================================
# FINANCIAL REPORTS
# =====================================================


def trial_balance(
    db: Session
):

    ledgers = (
        db.query(GeneralLedger)
        .all()
    )


    total_debit = 0
    total_credit = 0


    accounts = []


    for ledger in ledgers:

        balance = ledger.balance or 0


        if balance >= 0:

            debit = balance
            credit = 0

        else:

            debit = 0
            credit = abs(balance)


        total_debit += debit
        total_credit += credit


        accounts.append(
            {
                "account": ledger.account_name,
                "debit": debit,
                "credit": credit
            }
        )


    return {
        "accounts": accounts,
        "total_debit": total_debit,
        "total_credit": total_credit
    }



def profit_loss(
    db: Session
):

    ledgers = (
        db.query(GeneralLedger)
        .all()
    )


    revenue = 0
    expenses = 0


    for ledger in ledgers:

        if ledger.account_type == "REVENUE":

            revenue += ledger.balance


        elif ledger.account_type == "EXPENSE":

            expenses += ledger.balance



    return {

        "revenue": revenue,

        "expenses": expenses,

        "profit": revenue - expenses
    }



def balance_sheet(
    db: Session
):

    assets = 0
    liabilities = 0


    # Accounts Receivable = Asset

    receivables = (
        db.query(
            AccountsReceivable
        )
        .all()
    )


    for item in receivables:

        assets += (
            item.amount -
            item.received_amount
        )



    # Accounts Payable = Liability

    payables = (
        db.query(
            AccountsPayable
        )
        .all()
    )


    for item in payables:

        liabilities += (
            item.amount -
            item.paid_amount
        )



    return {

        "assets": assets,

        "liabilities": liabilities,

        "equity": assets - liabilities

    }