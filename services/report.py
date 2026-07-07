from sqlalchemy.orm import Session

from models.report import Report

from repositories.report import (
    report_repository
)

from schemas.report import (
    ReportCreate
)



def create_report(
    db: Session,
    data: ReportCreate
):

    report = Report(

        report_name=data.report_name,

        report_type=data.report_type,

        generated_by=data.generated_by
    )

    return report_repository.create(
        db,
        report
    )



def get_reports(
    db: Session
):

    return report_repository.get_all(db)