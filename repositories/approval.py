from sqlalchemy.orm import Session

from models.approval import Approval


class ApprovalRepository:


    def create(
        self,
        db: Session,
        approval: Approval
    ):

        db.add(approval)
        db.commit()
        db.refresh(approval)

        return approval



    def get_all(
        self,
        db: Session
    ):

        return db.query(Approval).all()



    def get(
        self,
        db: Session,
        approval_id: int
    ):

        return db.query(Approval).filter(
            Approval.id == approval_id
        ).first()



    def update(
        self,
        db: Session,
        approval: Approval
    ):

        db.commit()
        db.refresh(approval)

        return approval



approval_repository = ApprovalRepository()