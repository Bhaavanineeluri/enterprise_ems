import os

from fastapi import HTTPException, UploadFile

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



UPLOAD_FOLDER = "uploads/documents"



# =====================================================
# FILE UPLOAD + CREATE DOCUMENT
# =====================================================

def upload_document(
    db: Session,
    file: UploadFile,
    data: DocumentCreate
):

    if not os.path.exists(UPLOAD_FOLDER):

        os.makedirs(
            UPLOAD_FOLDER
        )


    file_extension = (
        os.path.splitext(file.filename)[1]
    )


    file_location = (
        f"{UPLOAD_FOLDER}/{file.filename}"
    )


    with open(
        file_location,
        "wb"
    ) as buffer:

        buffer.write(
            file.file.read()
        )


    file_size = os.path.getsize(
        file_location
    )


    document = Document(

        user_id=data.user_id,

        document_name=data.document_name,

        document_type=data.document_type,

        file_path=file_location,

        file_extension=file_extension,

        file_size=file_size,

        description=data.description,

        tags=data.tags,

        is_public=data.is_public,

        uploaded_by=data.user_id
    )


    return document_repository.create(
        db,
        document
    )



# =====================================================
# CREATE DOCUMENT (OLD SUPPORT)
# =====================================================

def create_document(
    db: Session,
    data: DocumentCreate
):

    document = Document(

        user_id=data.user_id,

        document_name=data.document_name,

        document_type=data.document_type,

        description=data.description,

        tags=data.tags,

        is_public=data.is_public
    )


    return document_repository.create(
        db,
        document
    )



# =====================================================
# GET ALL DOCUMENTS
# =====================================================

def get_documents(
    db: Session
):

    return document_repository.get_all(
        db
    )



# =====================================================
# GET DOCUMENT BY ID
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
# CREATE DOCUMENT VERSION
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
# GET DOCUMENT VERSIONS
# =====================================================

def get_document_versions(
    db: Session,
    document_id:int
):

    return document_repository.get_versions(
        db,
        document_id
    )



# =====================================================
# DELETE DOCUMENT FILE
# =====================================================

def delete_document_file(
    file_path:str
):

    if os.path.exists(file_path):

        os.remove(
            file_path
        )