from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.report import (
    ReportCreate
)

from services.report import (
    create_report,
    get_reports
)


router = APIRouter(

    prefix="/reports",

    tags=["Reports"]
)


@router.post("/")
def create(

    data: ReportCreate,

    db: Session = Depends(get_db)
):

    return create_report(
        db,
        data
    )


@router.get("/")
def all_reports(

    db: Session = Depends(get_db)
):

    return get_reports(db)