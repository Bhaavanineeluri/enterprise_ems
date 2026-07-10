from fastapi import FastAPI

from core.config import settings

from core.exceptions.custom import AppException
from core.exceptions.handler import (
    app_exception_handler,
    global_exception_handler
)

from middleware.security import SecurityHeadersMiddleware


# ---------------- AUTH / CORE ----------------
from routers.auth import router as auth_router



# ---------------- ORG STRUCTURE ----------------
from routers.company import router as company_router
from routers.branch import router as branch_router
from routers.department import router as department_router
from routers.team import router as team_router


from routers.finance import router as finance_router
# ---------------- USERS ----------------
from routers.user_router import router as user_router
from routers.employee import router as employee_router


# ---------------- BUSINESS MODULES ----------------
from routers.customer import router as customer_router
from routers.vendor import router as vendor_router
from routers.product import router as product_router
from routers.inventory import router as inventory_router
from routers.purchase import router as purchase_router
from routers.goods_receipt import router as goods_receipt_router
from routers.sales import router as sales_router
from routers.shipping import router as shipping_router

from routers.tenant import router as tenant_router

# ---------------- ENTERPRISE FEATURES ----------------
from routers.workflow import router as workflow_router
from routers.notification import router as notification_router
from routers.document import router as document_router
from routers.search import router as search_router
from routers.report import router as report_router
from routers.dashboard import router as dashboard_router
from routers.background import router as background_router


# ---------------- SYSTEM ----------------
from routers.health import router as health_router



# ---------------- APP INIT ----------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


# ---------------- API VERSION ----------------

API_PREFIX = "/api/v1"



# ---------------- EXCEPTION HANDLERS ----------------

app.add_exception_handler(
    AppException,
    app_exception_handler
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)



# ---------------- MIDDLEWARE ----------------

app.add_middleware(
    SecurityHeadersMiddleware
)



# ---------------- ROUTER REGISTRATION ----------------

app.include_router(
    auth_router,
    prefix=API_PREFIX
)
app.include_router(
    finance_router,
    prefix=API_PREFIX
)


app.include_router(
    user_router,
    prefix=API_PREFIX
)

app.include_router(
    employee_router,
    prefix=API_PREFIX
)


app.include_router(
    company_router,
    prefix=API_PREFIX
)

app.include_router(
    branch_router,
    prefix=API_PREFIX
)

app.include_router(
    department_router,
    prefix=API_PREFIX
)

app.include_router(
    team_router,
    prefix=API_PREFIX
)





app.include_router(
    customer_router,
    prefix=API_PREFIX
)

app.include_router(
    vendor_router,
    prefix=API_PREFIX
)

app.include_router(
    product_router,
    prefix=API_PREFIX
)

app.include_router(
    inventory_router,
    prefix=API_PREFIX
)


app.include_router(
    purchase_router,
    prefix=API_PREFIX
)

app.include_router(
    goods_receipt_router,
    prefix=API_PREFIX
)

app.include_router(
    sales_router,
    prefix=API_PREFIX
)

app.include_router(
    shipping_router,
    prefix=API_PREFIX
)

app.include_router(
    finance_router,
    prefix=API_PREFIX
)



app.include_router(
    workflow_router,
    prefix=API_PREFIX
)

app.include_router(
    notification_router,
    prefix=API_PREFIX
)

app.include_router(
    document_router,
    prefix=API_PREFIX
)

app.include_router(
    search_router,
    prefix=API_PREFIX
)

app.include_router(
    report_router,
    prefix=API_PREFIX
)

app.include_router(
    dashboard_router,
    prefix=API_PREFIX
)

app.include_router(
    background_router,
    prefix=API_PREFIX
)


app.include_router(
    health_router,
    prefix=API_PREFIX
)



# ---------------- HEALTH CHECK ----------------

@app.get("/")
def home():
    return {
        "message": "Enterprise Management System API Running Successfully"
    }