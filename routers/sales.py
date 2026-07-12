from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.sales import (
    QuotationCreate,
    SalesOrderCreate,
    InvoiceCreate
)

from services.sales import (
    create_quotation,
    create_sales_order,
    create_invoice,
    get_quotations,
    get_sales_orders,
    get_invoices
)

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


# =====================================================
# QUOTATION
# =====================================================

@router.post(
    "/quotations",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("sales", "create"))
    ]
)
def create_new_quotation(
    data: QuotationCreate,
    db: Session = Depends(get_db)
):
    return create_quotation(db, data)


@router.get(
    "/quotations",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("sales", "view"))
    ]
)
def list_quotations(
    db: Session = Depends(get_db)
):
    return get_quotations(db)


# =====================================================
# SALES ORDER
# =====================================================

@router.post(
    "/orders",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("sales", "create"))
    ]
)
def create_new_sales_order(
    data: SalesOrderCreate,
    db: Session = Depends(get_db)
):
    return create_sales_order(db, data)


@router.get(
    "/orders",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("sales", "view"))
    ]
)
def list_sales_orders(
    db: Session = Depends(get_db)
):
    return get_sales_orders(db)


# =====================================================
# INVOICE
# =====================================================

@router.post(
    "/invoices",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("sales", "create"))
    ]
)
def create_new_invoice(
    data: InvoiceCreate,
    db: Session = Depends(get_db)
):
    return create_invoice(db, data)


@router.get(
    "/invoices",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("sales", "view"))
    ]
)
def list_invoices(
    db: Session = Depends(get_db)
):
    return get_invoices(db)