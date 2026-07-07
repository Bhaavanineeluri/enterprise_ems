from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db


from schemas.document import (
    DocumentCreate,
    DocumentVersionCreate
)


from services.document import (
    create_document,
    get_documents,
    get_document,
    create_document_version,
    get_document_versions
)



router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)



@router.post("/")
def add_document(
    data: DocumentCreate,
    db: Session = Depends(get_db)
):

    return create_document(
        db,
        data
    )



@router.get("/")
def list_documents(
    db: Session = Depends(get_db)
):

    return get_documents(db)



@router.get("/{document_id}")
def fetch_document(
    document_id:int,
    db: Session = Depends(get_db)
):

    return get_document(
        db,
        document_id
    )



@router.post("/versions")
def add_version(
    data: DocumentVersionCreate,
    db: Session = Depends(get_db)
):

    return create_document_version(
        db,
        data
    )



@router.get("/{document_id}/versions")
def list_versions(
    document_id:int,
    db: Session = Depends(get_db)
):

    return get_document_versions(
        db,
        document_id
    )