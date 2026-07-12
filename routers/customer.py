from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)
from schemas.lead import (
    LeadCreate,
    LeadUpdate,
    LeadResponse
)

from services.lead import (
    create_lead,
    get_leads,
    update_lead
)
from services.customer import (
    create_customer,
    get_customers,
    get_all_customers,
    get_customer,
    update_customer,
    delete_customer
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


# =====================================================
# CREATE CUSTOMER
# =====================================================

@router.post(
    "/",
    response_model=CustomerResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("customer", "create"))
    ]
)
def create(
    data: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer(db, data)


# =====================================================
# LIST CUSTOMERS
# =====================================================

@router.get(
    "/",
    response_model=list[CustomerResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("customer", "view"))
    ]
)
def list_all(
    db: Session = Depends(get_db)
):
    return get_customers(db)


# =====================================================
# GET CUSTOMER
# =====================================================

@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("customer", "view"))
    ]
)
def get_one(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_customer(
        db,
        customer_id,
        current_user
    )


# =====================================================
# UPDATE CUSTOMER
# =====================================================

@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("customer", "update"))
    ]
)
def update_customer_by_id(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_customer(
        customer_id,
        customer,
        db,
        current_user
    )


# =====================================================
# DELETE CUSTOMER
# =====================================================

@router.delete(
    "/{customer_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("customer", "delete"))
    ]
)
def delete(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return delete_customer(
        db,
        customer_id,
        current_user
    )


# =====================================================
# LEGACY LIST
# =====================================================

@router.get(
    "/all",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("customer", "view"))
    ]
)
def read_all_customers(
    db: Session = Depends(get_db)
):
    return get_all_customers(db)


# =====================================================
# CUSTOMER LEADS
# =====================================================

@router.post(
    "/leads",
    response_model=LeadResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("lead", "create"))
    ]
)
def create_customer_lead(
    data: LeadCreate,
    db: Session = Depends(get_db)
):
    return create_lead(
        db,
        data
    )


@router.get(
    "/leads",
    response_model=list[LeadResponse],
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("lead", "view"))
    ]
)
def list_customer_leads(
    db: Session = Depends(get_db)
):
    return get_leads(db)


@router.put(
    "/leads/{lead_id}",
    response_model=LeadResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("lead", "update"))
    ]
)
def update_customer_lead(
    lead_id: int,
    data: LeadUpdate,
    db: Session = Depends(get_db)
):
    return update_lead(
        db,
        lead_id,
        data
    )