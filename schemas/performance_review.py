from pydantic import BaseModel, ConfigDict


class PerformanceReviewCreate(BaseModel):

    employee_id: int

    review_period: str

    reviewer: str

    rating: int

    comments: str


class PerformanceReviewResponse(PerformanceReviewCreate):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int