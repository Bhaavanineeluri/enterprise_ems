from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.report import ReportCreate

from services.report import (
    create_report,
    get_reports,
    get_report
)

from services.report_export import (
    export_csv,
    export_excel,
    export_pdf
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# ==========================
# CREATE REPORT
# ==========================

@router.post(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "create"))
    ]
)
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

@router.get(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "view"))
    ]
)
def all_reports(
    db: Session = Depends(get_db)
):
    return get_reports(db)


# ==========================
# GET REPORT BY ID
# ==========================

@router.get(
    "/{report_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "view"))
    ]
)
def report_by_id(
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

    return report


# ==========================
# KPI DASHBOARD
# ==========================

@router.get(
    "/dashboard/kpis",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "view"))
    ]
)
def report_kpis(
    db: Session = Depends(get_db)
):
    from models.customer import Customer
    from models.product import Product
    from models.employee import Employee
    from models.vendor import Vendor

    return {
        "total_customers": db.query(Customer).count(),
        "total_products": db.query(Product).count(),
        "total_employees": db.query(Employee).count(),
        "total_vendors": db.query(Vendor).count()
    }


# ==========================
# EXPORT CSV
# ==========================

@router.get(
    "/{report_id}/export/csv",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "export"))
    ]
)
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

@router.get(
    "/{report_id}/export/excel",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "export"))
    ]
)
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

@router.get(
    "/{report_id}/export/pdf",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("report", "export"))
    ]
)
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