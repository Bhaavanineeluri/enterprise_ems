from sqlalchemy.orm import Session

import json

from models.report import Report

from repositories.report import (
    report_repository
)

from schemas.report import (
    ReportCreate
)



# ==========================
# CREATE REPORT
# ==========================

def create_report(
    db: Session,
    data: ReportCreate
):

    report = Report(

        report_name=data.report_name,

        report_type=data.report_type,

        generated_by=data.generated_by,

        filters=json.dumps(data.filters)
        if data.filters
        else None
    )


    return report_repository.create(
        db,
        report
    )



# ==========================
# GET ALL REPORTS
# ==========================

def get_reports(
    db: Session
):

    return report_repository.get_all(db)



# ==========================
# GET REPORT BY ID
# ==========================

def get_report(
    db: Session,
    report_id: int
):

    return report_repository.get(
        db,
        report_id
    )



# ==========================
# UPDATE EXPORT DETAILS
# ==========================

def update_report_export(
    db: Session,
    report_id: int,
    file_path: str,
    export_format: str
):

    report = report_repository.get(
        db,
        report_id
    )


    if not report:
        return None


    report.file_path = file_path

    report.export_format = export_format

    report.status = "Completed"


    return report_repository.update(
        db,
        report
    )