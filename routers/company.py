from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.company import CompanyCreate, CompanyResponse

from services.company import (
    create_company,
    get_all_companies,
    get_company,
    delete_company
)
router = APIRouter(prefix="/companies", tags=["Company"])


@router.post("/", response_model=CompanyResponse)
def create(data: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db, data)


@router.get("/", response_model=list[CompanyResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_companies(db)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_one(company_id: int, db: Session = Depends(get_db)):
    return get_company(db, company_id)

@router.delete("/{company_id}")
def delete(
    company_id: int,
    db: Session = Depends(get_db)
):

    return delete_company(
        db,
        company_id
    )