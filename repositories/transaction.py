from models.transaction import Transaction


class TransactionRepository:


    def create(
        self,
        db,
        transaction
    ):

        db.add(transaction)
        db.flush()

        return transaction


    def get_all(
        self,
        db
    ):

        return db.query(Transaction).all()