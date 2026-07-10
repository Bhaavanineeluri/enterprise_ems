from sqlalchemy.orm import Session

from models.general_ledger import GeneralLedger


class GeneralLedgerRepository:

    def create(
        self,
        db: Session,
        ledger: GeneralLedger
    ):
        db.add(ledger)
        db.commit()
        db.refresh(ledger)
        return ledger


    def get(
        self,
        db: Session,
        ledger_id: int
    ):
        return (
            db.query(GeneralLedger)
            .filter(
                GeneralLedger.id == ledger_id
            )
            .first()
        )


    def get_all(
        self,
        db: Session
    ):
        return (
            db.query(GeneralLedger)
            .order_by(GeneralLedger.account_name)
            .all()
        )


    def update(
        self,
        db: Session,
        ledger: GeneralLedger
    ):
        db.commit()
        db.refresh(ledger)
        return ledger


    def delete(
        self,
        db: Session,
        ledger: GeneralLedger
    ):
        db.delete(ledger)
        db.commit()


general_ledger_repository = GeneralLedgerRepository()