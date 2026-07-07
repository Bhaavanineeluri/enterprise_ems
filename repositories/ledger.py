from models.ledger import Ledger


class LedgerRepository:


    def create(
        self,
        db,
        ledger
    ):

        db.add(ledger)
        db.flush()

        return ledger


    def get_all(
        self,
        db
    ):

        return db.query(Ledger).all()