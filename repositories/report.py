from sqlalchemy.orm import Session

from models.report import Report



class ReportRepository:


    # ==========================
    # CREATE REPORT
    # ==========================

    def create(
        self,
        db: Session,
        report: Report
    ):

        db.add(report)

        db.commit()

        db.refresh(report)

        return report



    # ==========================
    # GET ALL REPORTS
    # ==========================

    def get_all(
        self,
        db: Session
    ):

        return db.query(
            Report
        ).all()



    # ==========================
    # GET REPORT BY ID
    # ==========================

    def get(
        self,
        db: Session,
        report_id: int
    ):

        return db.query(
            Report
        ).filter(
            Report.id == report_id
        ).first()



    # ==========================
    # UPDATE REPORT
    # ==========================

    def update(
        self,
        db: Session,
        report: Report
    ):

        db.commit()

        db.refresh(report)

        return report



report_repository = ReportRepository()