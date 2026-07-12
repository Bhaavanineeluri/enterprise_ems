from pydantic import BaseModel, ConfigDict


class LeadCreate(BaseModel):

    first_name: str
    last_name: str | None = None
    company_name: str | None = None

    email: str
    phone: str | None = None

    source: str | None = None

    assigned_to: int | None = None


class LeadUpdate(BaseModel):

    first_name: str | None = None
    last_name: str | None = None
    company_name: str | None = None

    email: str | None = None
    phone: str | None = None

    source: str | None = None

    status: str | None = None

    assigned_to: int | None = None


class LeadResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    first_name: str
    last_name: str | None

    company_name: str | None

    email: str
    phone: str | None

    source: str | None

    status: str

    assigned_to: int | None