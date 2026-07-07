from fastapi import HTTPException
from sqlalchemy.orm import Session


from models.document import Document
from models.document_version import DocumentVersion


from repositories.document import (
    document_repository
)


from schemas.document import (
    DocumentCreate,
    DocumentVersionCreate
)



# =====================================================
# CREATE DOCUMENT
# =====================================================

def create_document(
    db: Session,
    data: DocumentCreate
):


    document = Document(

        user_id=data.user_id,

        document_name=data.document_name,

        document_type=data.document_type,

        file_path=data.file_path,

        is_public=data.is_public
    )


    return document_repository.create(
        db,
        document
    )



# =====================================================
# GET DOCUMENTS
# =====================================================

def get_documents(
    db: Session
):

    return document_repository.get_all(db)



# =====================================================
# GET DOCUMENT
# =====================================================

def get_document(
    db: Session,
    document_id:int
):

    document = document_repository.get(
        db,
        document_id
    )


    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )


    return document



# =====================================================
# CREATE VERSION
# =====================================================

def create_document_version(
    db: Session,
    data: DocumentVersionCreate
):


    document = document_repository.get(
        db,
        data.document_id
    )


    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )



    version = DocumentVersion(

        document_id=data.document_id,

        version_number=data.version_number,

        file_path=data.file_path,

        uploaded_by=data.uploaded_by
    )


    return document_repository.create_version(
        db,
        version
    )



# =====================================================
# GET VERSIONS
# =====================================================

def get_document_versions(
    db: Session,
    document_id:int
):

    return document_repository.get_versions(
        db,
        document_id
    )