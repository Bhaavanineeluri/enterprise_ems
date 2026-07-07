from fastapi import FastAPI

from database import Base, engine
from core.exceptions.custom import AppException
from core.exceptions.handler import (
    app_exception_handler,
    global_exception_handler
)
# ---------------- AUTH / CORE ----------------
from routers.auth import router as auth_router
from routers.login_history import router as login_history_router

# ---------------- ORG STRUCTURE ----------------
from routers.company import router as company_router
from routers.branch import router as branch_router
from routers.department import router as department_router
from routers.team import router as team_router
from routers.user_assignment import router as user_assignment_router

# ---------------- USERS ----------------
from routers.user_router import router as user_router

# ---------------- PHASE 13–16 MODULES ----------------
from routers.customer import router as customer_router
from routers.vendor import router as vendor_router
from routers.product import router as product_router
from routers.inventory import router as inventory_router
from routers.purchase import router as purchase_router
from routers.goods_receipt import router as goods_receipt_router
from routers.sales import router as sales_router
from routers.shipping import router as shipping_router
from routers.finance import router as finance_router

from routers.workflow import router as workflow_router
from routers.notification import router as notification_router
from routers.document import router as document_router
from routers.search import router as search_router
from routers.report import router as report_router
from routers.dashboard import router as dashboard_router
from routers.background import router as background_router

# ---------------- CREATE TABLES ----------------
Base.metadata.create_all(bind=engine)

# ---------------- APP INIT ----------------
from core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
# ---------------- ROUTER REGISTRATION ----------------
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(login_history_router)
app.add_exception_handler(
    AppException,
    app_exception_handler
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)
app.include_router(company_router)
app.include_router(branch_router)
app.include_router(department_router)
app.include_router(team_router)
app.include_router(user_assignment_router)

app.include_router(customer_router)
app.include_router(vendor_router)
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(purchase_router)
app.include_router(goods_receipt_router)
app.include_router(sales_router)
app.include_router(shipping_router)
app.include_router(finance_router)
app.include_router(workflow_router)
app.include_router(notification_router)
app.include_router(document_router)
app.include_router(search_router)
app.include_router(report_router)
app.include_router(dashboard_router)
app.include_router(background_router)



# ---------------- HEALTH CHECK ----------------
@app.get("/")
def home():
    return {
        "message": "Enterprise Management System API Running Successfully"
    }