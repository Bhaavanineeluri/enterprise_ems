from sqlalchemy.orm import Session

from models.user import User
from models.customer import Customer
from models.employee import Employee
from models.product import Product
from models.vendor import Vendor
from models.purchase_order import PurchaseOrder
from models.sales_order import SalesOrder
from models.invoice import Invoice


def get_dashboard(db: Session):

    return {

        "total_users":
        db.query(User).count(),

        "total_customers":
        db.query(Customer).count(),

        "total_employees":
        db.query(Employee).count(),

        "total_products":
        db.query(Product).count(),

        "total_vendors":
        db.query(Vendor).count(),

        "total_purchase_orders":
        db.query(PurchaseOrder).count(),

        "total_sales_orders":
        db.query(SalesOrder).count(),

        "total_invoices":
        db.query(Invoice).count()

    }