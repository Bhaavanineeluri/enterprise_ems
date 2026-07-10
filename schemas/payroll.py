from pydantic import BaseModel, ConfigDict


class PayrollCreate(BaseModel):

    employee_id: int

    basic_salary: float

    bank_name: str

    account_number: str


class PayrollResponse(PayrollCreate):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    payment_status: str