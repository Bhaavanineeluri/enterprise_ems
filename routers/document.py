import os

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form
)

from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from models.document import Document

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

UPLOAD_DIR = "uploads/documents"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


# ===============================
# CREATE DOCUMENT
# ===============================

@router.post(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("document", "create"))
    ]
)
def add_document(
    data: DocumentCreate,
    db: Session = Depends(get_db)
):
    return create_document(
        db,
        data
    )


# ===============================
# GET ALL DOCUMENTS
# ===============================

@router.get(
    "/",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("document", "view"))
    ]
)
def list_documents(
    db: Session = Depends(get_db)
):
    return get_documents(db)


# ===============================
# GET SINGLE DOCUMENT
# ===============================

@router.get(
    "/{document_id}",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("document", "view"))
    ]
)
def fetch_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    return get_document(
        db,
        document_id
    )


# ===============================
# CREATE DOCUMENT VERSION
# ===============================

@router.post(
    "/versions",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("document", "update"))
    ]
)
def add_version(
    data: DocumentVersionCreate,
    db: Session = Depends(get_db)
):
    return create_document_version(
        db,
        data
    )


# ===============================
# GET DOCUMENT VERSIONS
# ===============================

@router.get(
    "/{document_id}/versions",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("document", "view"))
    ]
)
def list_versions(
    document_id: int,
    db: Session = Depends(get_db)
):
    return get_document_versions(
        db,
        document_id
    )


# ===============================
# UPLOAD DOCUMENT
# ===============================

@router.post(
    "/upload",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("document", "upload"))
    ]
)
def upload_document(
    user_id: int = Form(...),
    document_name: str = Form(...),
    document_type: str = Form(...),
    description: str = Form(None),
    tags: str = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    file_location = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    file_size = os.path.getsize(file_location)

    extension = (
        file.filename.split(".")[-1]
        if "." in file.filename
        else None
    )

    document = Document(
        user_id=user_id,
        uploaded_by=user_id,
        document_name=document_name,
        document_type=document_type,
        file_path=file_location,
        description=description,
        tags=tags,
        file_extension=extension,
        file_size=file_size,
        mime_type=file.content_type
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document