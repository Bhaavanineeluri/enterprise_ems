from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from fastapi.responses import FileResponse
from fastapi import HTTPException

from services.report_export import (
    export_csv,
    export_excel,
    export_pdf
)
from schemas.report import (
    ReportCreate
)
from sqlalchemy.orm import Session

from database import get_db


from services.report import (
    create_report,
    get_reports,
    get_report
)


from services.report import (
    create_report,
    get_reports,
    get_report
)



router = APIRouter(

    prefix="/reports",

    tags=["Reports"]
)



# ==========================
# CREATE REPORT
# ==========================

@router.post("/")
def create(

    data: ReportCreate,

    db: Session = Depends(get_db)

):

    return create_report(
        db,
        data
    )



# ==========================
# GET ALL REPORTS
# ==========================

@router.get("/")
def all_reports(

    db: Session = Depends(get_db)

):

    return get_reports(db)



# ==========================
# GET REPORT BY ID
# ==========================

@router.get("/{report_id}")
def report_by_id(

    report_id:int,

    db: Session = Depends(get_db)

):

    report = get_report(
        db,
        report_id
    )


    if not report:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )


    return report



# ==========================
# KPI DASHBOARD
# ==========================

@router.get("/dashboard/kpis")
def report_kpis(

    db: Session = Depends(get_db)

):

    from models.customer import Customer
    from models.product import Product
    from models.employee import Employee
    from models.vendor import Vendor


    return {

        "total_customers":
            db.query(Customer).count(),


        "total_products":
            db.query(Product).count(),


        "total_employees":
            db.query(Employee).count(),


        "total_vendors":
            db.query(Vendor).count()

    }
# ==========================
# EXPORT CSV
# ==========================

@router.get("/{report_id}/export/csv")
def export_report_csv(

    report_id: int,

    db: Session = Depends(get_db)

):

    report = get_report(
        db,
        report_id
    )


    if not report:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )


    file_path = export_csv(
        report_id,
        [report.report_name, report.report_type]
    )


    return FileResponse(
        file_path,
        media_type="text/csv",
        filename=f"report_{report_id}.csv"
    )



# ==========================
# EXPORT EXCEL
# ==========================

@router.get("/{report_id}/export/excel")
def export_report_excel(

    report_id: int,

    db: Session = Depends(get_db)

):

    report = get_report(
        db,
        report_id
    )


    if not report:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )


    file_path = export_excel(
        report_id,
        [report.report_name, report.report_type]
    )


    return FileResponse(
        file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"report_{report_id}.xlsx"
    )



# ==========================
# EXPORT PDF
# ==========================

@router.get("/{report_id}/export/pdf")
def export_report_pdf(

    report_id: int,

    db: Session = Depends(get_db)

):

    report = get_report(
        db,
        report_id
    )


    if not report:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )


    file_path = export_pdf(
        report_id,
        [report.report_name, report.report_type]
    )


    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename=f"report_{report_id}.pdf"
    )