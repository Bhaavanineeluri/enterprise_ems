from sqlalchemy import or_
from sqlalchemy.orm import Session

from models.customer import Customer
from models.employee import Employee
from models.product import Product
from models.vendor import Vendor



# =====================================================
# GLOBAL SEARCH
# =====================================================

def global_search(
    db: Session,
    keyword: str
):

    customers = db.query(Customer).filter(
        or_(
            Customer.customer_name.ilike(f"%{keyword}%"),
            Customer.customer_code.ilike(f"%{keyword}%")
        )
    ).all()


    employees = db.query(Employee).filter(
        or_(
            Employee.employee_code.ilike(f"%{keyword}%"),
            Employee.designation.ilike(f"%{keyword}%")
        )
    ).all()


    products = db.query(Product).filter(
        or_(
            Product.product_name.ilike(f"%{keyword}%"),
            Product.product_code.ilike(f"%{keyword}%")
        )
    ).all()


    vendors = db.query(Vendor).filter(
        or_(
            Vendor.vendor_name.ilike(f"%{keyword}%"),
            Vendor.vendor_code.ilike(f"%{keyword}%")
        )
    ).all()


    return {

        "customers": customers,

        "employees": employees,

        "products": products,

        "vendors": vendors

    }