from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from services.dashboard import executive_dashboard,operational_dashboard,customer_widget,customer_growth_chart,employee_growth_chart,product_category_chart,inventory_status_chart,customer_forecast,sales_forecast,inventory_forecast


router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)


@router.get("/executive")
def get_executive_dashboard(
    db: Session = Depends(get_db)
):
    return executive_dashboard(db)

@router.get("/operational")
def get_operational_dashboard(
    db: Session = Depends(get_db)
):
    return operational_dashboard(db)

@router.get("/widgets/customers")
def customer_dashboard_widget(
    db: Session = Depends(get_db)
):
    return customer_widget(db)

@router.get("/charts/customers")
def customers_chart(db: Session = Depends(get_db)):
    return customer_growth_chart(db)


@router.get("/charts/employees")
def employees_chart(db: Session = Depends(get_db)):
    return employee_growth_chart(db)


@router.get("/charts/products")
def products_chart(db: Session = Depends(get_db)):
    return product_category_chart(db)


@router.get("/charts/inventory")
def inventory_chart(db: Session = Depends(get_db)):
    return inventory_status_chart(db)
@router.get("/forecast/customers")
def customer_forecast_api(
    db: Session = Depends(get_db)
):
    return customer_forecast(db)


@router.get("/forecast/sales")
def sales_forecast_api(
    db: Session = Depends(get_db)
):
    return sales_forecast(db)


@router.get("/forecast/inventory")
def inventory_forecast_api(
    db: Session = Depends(get_db)
):
    return inventory_forecast(db)