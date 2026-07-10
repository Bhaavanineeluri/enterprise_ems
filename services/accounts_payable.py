from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.accounts_payable import AccountsPayable

from repositories.accounts_payable import (
    accounts_payable_repository
)



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



def update_payment(
    db: Session,
    payable_id: int,
    paid_amount: float
):

    payable = accounts_payable_repository.get(
        db,
        payable_id
    )


    if not payable:

        raise HTTPException(
            status_code=404,
            detail="Payable record not found"
        )


    payable.paid_amount = paid_amount


    if paid_amount >= payable.amount:

        payable.status = "PAID"

    elif paid_amount > 0:

        payable.status = "PARTIALLY_PAID"

    else:

        payable.status = "PENDING"



    return accounts_payable_repository.update(
        db,
        payable
    )