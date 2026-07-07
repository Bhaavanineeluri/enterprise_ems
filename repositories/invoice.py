from models.invoice import Invoice


class InvoiceRepository:


    def create(
        self,
        db,
        invoice
    ):

        db.add(invoice)
        db.flush()

        return invoice


    def get_all(
        self,
        db
    ):

        return db.query(Invoice).all()


    def get(
        self,
        db,
        invoice_id
    ):

        return db.query(Invoice).filter(
            Invoice.id == invoice_id
        ).first()