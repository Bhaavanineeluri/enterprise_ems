from sqlalchemy.orm import Session

from models.document import Document
from models.document_version import DocumentVersion



class DocumentRepository:


    # ============================
    # DOCUMENT
    # ============================

    def create(
        self,
        db: Session,
        document: Document
    ):

        db.add(document)
        db.commit()
        db.refresh(document)

        return document



    def get_all(
        self,
        db: Session
    ):

        return db.query(Document).all()



    def get(
        self,
        db: Session,
        document_id: int
    ):

        return db.query(Document).filter(
            Document.id == document_id
        ).first()



    # ============================
    # VERSION
    # ============================

    def create_version(
        self,
        db: Session,
        version: DocumentVersion
    ):

        db.add(version)
        db.commit()
        db.refresh(version)

        return version



    def get_versions(
        self,
        db: Session,
        document_id: int
    ):

        return db.query(
            DocumentVersion
        ).filter(
            DocumentVersion.document_id == document_id
        ).all()



document_repository = DocumentRepository()