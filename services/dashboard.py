from datetime import date, datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from models.user import User
from models.company import Company
from models.branch import Branch
from models.department import Department
from models.team import Team

from models.employee import Employee
from models.attendance import Attendance
from models.leave import Leave

from models.customer import Customer
from models.vendor import Vendor

from models.product import Product
from models.inventory import Inventory

from models.purchase_order import PurchaseOrder
from models.sales_order import SalesOrder
from models.shipment import Shipment

from models.invoice import Invoice
from models.payment import Payment

from models.approval import Approval
from models.notification import Notification
def executive_dashboard(db: Session):

    return {
        "users": db.query(func.count(User.id)).scalar(),
        "employees": db.query(func.count(Employee.id)).scalar(),
        "customers": db.query(func.count(Customer.id)).scalar(),
        "vendors": db.query(func.count(Vendor.id)).scalar(),
        "companies": db.query(func.count(Company.id)).scalar(),
        "branches": db.query(func.count(Branch.id)).scalar(),
        "departments": db.query(func.count(Department.id)).scalar(),
        "teams": db.query(func.count(Team.id)).scalar(),
        "products": db.query(func.count(Product.id)).scalar(),
        
        "purchase_orders": db.query(func.count(PurchaseOrder.id)).scalar(),
        "sales_orders": db.query(func.count(SalesOrder.id)).scalar(),
        "invoices": db.query(func.count(Invoice.id)).scalar(),
        "payments": db.query(func.count(Payment.id)).scalar()
    }




def operational_dashboard(db: Session):

    today = date.today()

    total_employees = db.query(func.count(Employee.id)).scalar()

    present_today = (
        db.query(func.count(Attendance.id))
        .filter(Attendance.attendance_date == today)
        .scalar()
    )

    leave_today = (
        db.query(func.count(Leave.id))
        .filter(Leave.status == "Approved")
        .scalar()
    )

    low_stock = (
    db.query(Inventory)
    .join(Product)
    .filter(
        Inventory.quantity < Product.minimum_stock
    )
    .count()
    )

    orders = db.query(func.count(SalesOrder.id)).scalar()

    shipments = db.query(func.count(Shipment.id)).scalar()

    payments = db.query(func.count(Payment.id)).scalar()

    approvals = (
        db.query(func.count(Approval.id))
        .filter(
            Approval.status == "Pending"
        )
        .scalar()
    )

    notifications = (
        db.query(func.count(Notification.id))
        .scalar()
    )

    return {
        "employees": {
            "total": total_employees,
            "present_today": present_today,
            "on_leave": leave_today
        },
        "inventory": {
            "low_stock": low_stock
        },
        "sales": {
            "orders": orders,
            "shipments": shipments
        },
        "finance": {
            "payments": payments
        },
        "workflow": {
            "pending_approvals": approvals
        },
        "notifications": notifications
    }



def customer_widget(db: Session):

    current_month = datetime.now().month
    current_year = datetime.now().year

    total_customers = db.query(func.count(Customer.id)).scalar()

    new_customers = (
        db.query(Customer)
        .filter(
            func.month(Customer.created_at) == current_month,
            func.year(Customer.created_at) == current_year
        )
        .count()
    )


    return {
        "total_customers": total_customers,
        "new_customers": new_customers,
        
    }


def customer_growth_chart(db: Session):

    data = (
        db.query(
            func.monthname(Customer.created_at).label("month"),
            func.count(Customer.id).label("customers")
        )
        .group_by(
            func.month(Customer.created_at),
            func.monthname(Customer.created_at)
        )
        .order_by(func.month(Customer.created_at))
        .all()
    )

    return [
        {
            "month": row.month,
            "customers": row.customers
        }
        for row in data
    ]



def employee_growth_chart(db: Session):

    data = (
        db.query(
            func.monthname(Employee.created_at).label("month"),
            func.count(Employee.id).label("employees")
        )
        .group_by(
            func.month(Employee.created_at),
            func.monthname(Employee.created_at)
        )
        .order_by(func.month(Employee.created_at))
        .all()
    )

    return [
        {
            "month": row.month,
            "employees": row.employees
        }
        for row in data
    ]



def product_category_chart(db: Session):

    data = (
        db.query(
            Product.category,
            func.count(Product.id)
        )
        .group_by(Product.category)
        .all()
    )

    return [
        {
            "category": row[0],
            "count": row[1]
        }
        for row in data
    ]



def inventory_status_chart(db: Session):

    low_stock = (
    db.query(Inventory)
    .join(Product)
    .filter(
        Inventory.quantity < Product.minimum_stock
    )
    .count()
    )

    out_of_stock = (
        db.query(Inventory)
        .filter(
            Inventory.quantity == 0
        )
        .count()
    )

    normal_stock = (
    db.query(Inventory)
    .join(Product)
    .filter(
        Inventory.quantity >= Product.minimum_stock
    )
    .count()
    )

    return {
        "low_stock": low_stock,
        "normal_stock": normal_stock,
        "out_of_stock": out_of_stock
    }


def inventory_forecast(db: Session):
    
    low_stock = (
        db.query(Inventory)
        .join(Product)
        .filter(
            Inventory.quantity > 0,
            Inventory.quantity <= Product.minimum_stock
        )
        .count()
    )

    out_of_stock = (
        db.query(Inventory)
        .filter(
            Inventory.quantity == 0
        )
        .count()
    )

    normal_stock = (
        db.query(Inventory)
        .join(Product)
        .filter(
            Inventory.quantity > Product.minimum_stock
        )
        .count()
    )

    recommended_restock = low_stock + out_of_stock

    return {
        "low_stock_products": low_stock,
        "normal_stock_products": normal_stock,
        "out_of_stock_products": out_of_stock,
        "recommended_restock": recommended_restock
    }

  
def sales_forecast(db: Session):

    current_year = datetime.now().year

    monthly_data = (
        db.query(
            func.month(SalesOrder.created_at).label("month"),
            func.count(SalesOrder.id).label("orders")
        )
        .filter(
            func.year(SalesOrder.created_at) == current_year
        )
        .group_by(func.month(SalesOrder.created_at))
        .order_by(func.month(SalesOrder.created_at))
        .all()
    )

    counts = [row.orders for row in monthly_data]

    if not counts:
        return {
            "average_orders": 0,
            "last_month_orders": 0,
            "forecast_next_month": 0,
            "trend": "stable"
        }

    average = sum(counts) / len(counts)

    last_month = counts[-1]

    if last_month > average:
        trend = "upward"
        forecast = round(last_month * 1.05)

    elif last_month < average:
        trend = "downward"
        forecast = round(last_month * 0.95)

    else:
        trend = "stable"
        forecast = round(last_month)

    return {
        "average_orders": round(average, 2),
        "last_month_orders": last_month,
        "forecast_next_month": forecast,
        "trend": trend
    }

def customer_forecast(db: Session):

    current_year = datetime.now().year

    monthly_data = (
        db.query(
            func.month(Customer.created_at).label("month"),
            func.count(Customer.id).label("count")
        )
        .filter(
            func.year(Customer.created_at) == current_year
        )
        .group_by(func.month(Customer.created_at))
        .all()
    )

    counts = [row.count for row in monthly_data]

    if not counts:
        return {
            "last_6_months_average": 0,
            "forecast_next_month": 0,
            "trend": "stable"
        }

    average = sum(counts) / len(counts)

    last_month = counts[-1]

    if last_month > average:
        trend = "upward"
        forecast = round(last_month * 1.05)

    elif last_month < average:
        trend = "downward"
        forecast = round(last_month * 0.95)

    else:
        trend = "stable"
        forecast = round(last_month)

    return {
        "last_6_months_average": round(average, 2),
        "forecast_next_month": forecast,
        "trend": trend
    }