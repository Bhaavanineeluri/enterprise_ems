from models.payment import Payment


class PaymentRepository:


    def create(
        self,
        db,
        payment
    ):

        db.add(payment)
        db.flush()

        return payment


    def get_all(
        self,
        db
    ):

        return db.query(Payment).all()


    def get(
        self,
        db,
        payment_id
    ):

        return db.query(Payment).filter(
            Payment.id == payment_id
        ).first()