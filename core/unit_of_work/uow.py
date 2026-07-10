from sqlalchemy.orm import Session

from repositories.user import user_repository
from repositories.customer import customer_repository
from repositories.employee import employee_repository

from repositories.company import company_repository
from repositories.branch import branch_repository
from repositories.department import department_repository
from repositories.team import team_repository

from repositories.vendor import vendor_repository
from repositories.product import product_repository
from repositories.inventory import inventory_repository

from repositories.purchase_request import purchase_request_repository
from repositories.purchase_order import purchase_order_repository
from repositories.goods_receipt import goods_receipt_repository

from repositories.invoice import InvoiceRepository
from repositories.payment import PaymentRepository
from repositories.transaction import TransactionRepository
from repositories.general_ledger import GeneralLedgerRepository
class UnitOfWork:

    def __init__(self, db: Session):

        self.db = db


        # User Management
        self.users = user_repository
        self.customers = customer_repository
        self.employees = employee_repository


        # Organization
        self.companies = company_repository
        self.branches = branch_repository
        self.departments = department_repository
        self.teams = team_repository


        # Inventory
        self.vendors = vendor_repository
        self.products = product_repository
        self.inventory = inventory_repository


        # Purchase
        self.purchase_requests = purchase_request_repository
        self.purchase_orders = purchase_order_repository
        self.goods_receipts = goods_receipt_repository

        self.invoices = InvoiceRepository()
        self.payments = PaymentRepository()
        self.transactions = TransactionRepository()
        self.ledgers = GeneralLedgerRepository()

    def commit(self):

        self.db.commit()



    def rollback(self):

        self.db.rollback()



    def refresh(self, obj):

        self.db.refresh(obj)



    def flush(self):

        self.db.flush()