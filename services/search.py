from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy import text

from models.employee import Employee
from models.customer import Customer
from models.company import Company
from models.vendor import Vendor
from models.product import Product
from models.user import User
from sqlalchemy import or_

from models.search_log import SearchLog

def global_search(
    db: Session,
    q: str,
    type: str | None = None,
    user_id: int | None = None
):
    # Save original search text
    search_text = q

    # Log the search
    log = SearchLog(
        user_id=user_id,
        search_query=search_text,
        module=type if type else "global"
    )

    db.add(log)
    

    # Now prepare for LIKE search
    q = f"%{search_text}%"

    employees = []

    if type in (None, "employee"):
        employees = (
            db.query(Employee)
            .join(User)
            .filter(
                or_(
                    Employee.employee_code.ilike(q),
                    Employee.designation.ilike(q),
                    User.full_name.ilike(q)
                )
            )
            .all()
        )

    customers = []

    if type in (None, "customer"):
        customers = (
            db.query(Customer)
            .filter(
                or_(
                    Customer.customer_code.ilike(q),
                    Customer.company_name.ilike(q)
                )
            )
            .all()
        )

    companies = []

    if type in (None, "company"):
        companies = (
            db.query(Company)
            .filter(
                or_(
                    Company.company_name.ilike(q),
                    Company.company_code.ilike(q)
                )
            )
            .all()
        )

    vendors = []

    if type in (None, "vendor"):
        vendors = (
            db.query(Vendor)
            .filter(
                or_(
                    Vendor.vendor_code.ilike(q),
                    Vendor.name.ilike(q)
                )
            )
            .all()
        )

    products = []

    if type in (None, "product"):
        products = (
            db.query(Product)
            .filter(
                or_(
                    Product.product_code.ilike(q),
                    Product.name.ilike(q)
                )
            )
            .all()
        )
    db.commit()
    return {
        "employees": [
            {
                "id": e.id,
                "code": e.employee_code,
                "name": e.user.full_name
            }
            for e in employees
        ],
        "customers": [
            {
                "id": c.id,
                "code": c.customer_code,
                "name": c.customer_name
            }
            for c in customers
        ],
        "companies": [
            {
                "id": c.id,
                "code": c.company_code,
                "name": c.company_name
            }
            for c in companies
        ],
        "vendors": [
            {
                "id": v.id,
                "code": v.vendor_code,
                "name": v.name
            }
            for v in vendors
        ],
        "products": [
            {
                "id": p.id,
                "code": p.product_code,
                "name": p.name
            }
            for p in products
        ],
    }

def autocomplete(db: Session, q: str):

    q = f"%{q}%"

    suggestions = []

    # Products
    products = (
        db.query(Product)
        .filter(Product.name.ilike(q))
        .limit(5)
        .all()
    )

    for product in products:
        suggestions.append({
            "type": "product",
            "id": product.id,
            "label": product.name
        })

    # Companies
    companies = (
        db.query(Company)
        .filter(Company.company_name.ilike(q))
        .limit(5)
        .all()
    )

    for company in companies:
        suggestions.append({
            "type": "company",
            "id": company.id,
            "label": company.company_name
        })

    # Customers
    customers = (
        db.query(Customer)
        .filter(Customer.company_name.ilike(q))
        .limit(5)
        .all()
    )

    for customer in customers:
        suggestions.append({
            "type": "customer",
            "id": customer.id,
            "label": customer.company_name
        })

    # Vendors
    vendors = (
        db.query(Vendor)
        .filter(Vendor.name.ilike(q))
        .limit(5)
        .all()
    )

    for vendor in vendors:
        suggestions.append({
            "type": "vendor",
            "id": vendor.id,
            "label": vendor.name
        })

    return {
        "suggestions": suggestions
    }


def fulltext_search(
    db: Session,
    q: str
):

    products = db.execute(
        text("""
            SELECT id, product_code, name
            FROM products
            WHERE MATCH(name, product_code)
            AGAINST(:q IN NATURAL LANGUAGE MODE)
        """),
        {"q": q}
    ).mappings().all()

    customers = db.execute(
        text("""
            SELECT id, customer_code, company_name
            FROM customers
            WHERE MATCH(company_name, customer_code)
            AGAINST(:q IN NATURAL LANGUAGE MODE)
        """),
        {"q": q}
    ).mappings().all()

    companies = db.execute(
        text("""
            SELECT id, company_code, company_name
            FROM companies
            WHERE MATCH(company_name, company_code)
            AGAINST(:q IN NATURAL LANGUAGE MODE)
        """),
        {"q": q}
    ).mappings().all()

    vendors = db.execute(
        text("""
            SELECT id, vendor_code, name
            FROM vendors
            WHERE MATCH(name, vendor_code)
            AGAINST(:q IN NATURAL LANGUAGE MODE)
        """),
        {"q": q}
    ).mappings().all()

    employees = db.execute(
        text("""
            SELECT
                e.id,
                e.employee_code,
                u.full_name
            FROM employees e
            JOIN users u
                ON e.user_id = u.id
            WHERE
                MATCH(e.employee_code, e.designation)
                AGAINST(:q IN NATURAL LANGUAGE MODE)
                OR
                MATCH(u.full_name)
                AGAINST(:q IN NATURAL LANGUAGE MODE)
        """),
        {"q": q}
    ).mappings().all()

    return {
        "employees": employees,
        "customers": customers,
        "companies": companies,
        "vendors": vendors,
        "products": products
    }