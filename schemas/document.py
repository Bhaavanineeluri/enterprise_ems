from pydantic import BaseModel, ConfigDict



class DocumentCreate(BaseModel):

    user_id: int
    document_name: str
    document_type: str
    file_path: str
    is_public: bool = False



class DocumentResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int
    user_id: int
    document_name: str
    document_type: str
    file_path: str
    
class DocumentVersionCreate(BaseModel):
    
    document_id: int
    version_number: int
    file_path: str
    uploaded_by: int