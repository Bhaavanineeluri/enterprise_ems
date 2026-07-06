from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.company import Company
from schemas.company import CompanyCreate


def create_company(db: Session, data: CompanyCreate):

    existing = db.query(Company).filter(
        Company.company_code == data.company_code
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Company code already exists"
        )

    company = Company(
        company_name=data.company_name,
        company_code=data.company_code,
        email=data.email,
        phone=data.phone,
        website=data.website,
        address=data.address
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return company


def get_all_companies(db: Session):
    return db.query(Company).all()


def get_company(db: Session, company_id: int):
    company = db.query(Company).filter(Company.id == company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company