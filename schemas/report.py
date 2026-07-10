from datetime import datetime

from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict



# ==========================
# CREATE REPORT
# ==========================

class ReportCreate(BaseModel):

    report_name: str

    report_type: str

    generated_by: str

    filters: Optional[Dict[str, Any]] = None



# ==========================
# REPORT RESPONSE
# ==========================

class ReportResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int

    report_name: str

    report_type: str

    generated_by: str

    filters: Optional[str] = None

    file_path: Optional[str] = None

    export_format: Optional[str] = None

    status: Optional[str] = None

    created_at: datetime



# ==========================
# EXPORT REQUEST
# ==========================

class ReportExportRequest(BaseModel):

    report_id: int

    export_format: str