from sqlalchemy.orm import Session

from models.report import Report


class ReportRepository:


    def create(
        self,
        db: Session,
        report: Report
    ):

        db.add(report)

        db.commit()

        db.refresh(report)

        return report


    def get_all(
        self,
        db: Session
    ):

        return db.query(
            Report
        ).all()


report_repository = ReportRepository()