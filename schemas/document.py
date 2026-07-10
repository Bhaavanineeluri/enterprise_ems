from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):

    document_name: str
    document_type: str

    description: str | None = None
    tags: str | None = None
    keywords: str | None = None

    is_public: bool = False
    access_level: str = "PRIVATE"



class DocumentVersionCreate(BaseModel):

    document_id: int

    version_number: int

    file_path: str

    description: str | None = None



class DocumentUploadResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    document_name: str

    document_type: str

    file_path: str

    description: str | None = None

    tags: str | None = None

    keywords: str | None = None

    file_size: int | None = None

    mime_type: str | None = None

    is_public: bool

    access_level: str

    ocr_status: str

    created_at: str | None = None