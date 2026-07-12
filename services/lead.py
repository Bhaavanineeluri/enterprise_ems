from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.unit_of_work.uow import UnitOfWork

from schemas.lead import (
    LeadCreate,
    LeadUpdate
)


# =====================================================
# CREATE LEAD
# =====================================================

def create_lead(
    db: Session,
    data: LeadCreate
):

    uow = UnitOfWork(db)

    existing = uow.leads.first_by(
        db,
        email=data.email
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Lead already exists"
        )

    try:

        lead = uow.leads.model(
            **data.model_dump()
        )

        uow.leads.create(
            db,
            lead
        )

        uow.commit()

        uow.refresh(lead)

        return lead

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# GET ALL LEADS
# =====================================================

def get_leads(
    db: Session
):

    uow = UnitOfWork(db)

    return uow.leads.get_all(db)


# =====================================================
# GET SINGLE LEAD
# =====================================================

def get_lead(
    db: Session,
    lead_id: int
):

    uow = UnitOfWork(db)

    lead = uow.leads.get(
        db,
        lead_id
    )

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return lead


# =====================================================
# UPDATE LEAD
# =====================================================

def update_lead(
    db: Session,
    lead_id: int,
    data: LeadUpdate
):

    uow = UnitOfWork(db)

    lead = uow.leads.get(
        db,
        lead_id
    )

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    update_data = data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            lead,
            key,
            value
        )

    return uow.leads.update(
        db,
        lead
    )


# =====================================================
# DELETE LEAD
# =====================================================

def delete_lead(
    db: Session,
    lead_id: int
):

    uow = UnitOfWork(db)

    lead = uow.leads.get(
        db,
        lead_id
    )

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    try:

        uow.leads.delete(
            db,
            lead
        )

        uow.commit()

        return {
            "success": True,
            "message": "Lead deleted successfully"
        }

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )