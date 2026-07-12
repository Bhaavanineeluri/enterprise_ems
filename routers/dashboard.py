from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from services.dashboard import (
    executive_dashboard,
    operational_dashboard,
    customer_widget,
    customer_growth_chart,
    employee_growth_chart,
    product_category_chart,
    inventory_status_chart,
    customer_forecast,
    sales_forecast,
    inventory_forecast
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/executive",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def get_executive_dashboard(
    db: Session = Depends(get_db)
):
    return executive_dashboard(db)


@router.get(
    "/operational",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def get_operational_dashboard(
    db: Session = Depends(get_db)
):
    return operational_dashboard(db)


@router.get(
    "/widgets/customers",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def customer_dashboard_widget(
    db: Session = Depends(get_db)
):
    return customer_widget(db)


@router.get(
    "/charts/customers",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def customers_chart(
    db: Session = Depends(get_db)
):
    return customer_growth_chart(db)


@router.get(
    "/charts/employees",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def employees_chart(
    db: Session = Depends(get_db)
):
    return employee_growth_chart(db)


@router.get(
    "/charts/products",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def products_chart(
    db: Session = Depends(get_db)
):
    return product_category_chart(db)


@router.get(
    "/charts/inventory",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def inventory_chart(
    db: Session = Depends(get_db)
):
    return inventory_status_chart(db)


@router.get(
    "/forecast/customers",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def customer_forecast_api(
    db: Session = Depends(get_db)
):
    return customer_forecast(db)


@router.get(
    "/forecast/sales",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def sales_forecast_api(
    db: Session = Depends(get_db)
):
    return sales_forecast(db)


@router.get(
    "/forecast/inventory",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("dashboard", "view"))
    ]
)
def inventory_forecast_api(
    db: Session = Depends(get_db)
):
    return inventory_forecast(db)