from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class PerformanceReview(Base):

    __tablename__ = "performance_reviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    review_period = Column(
        String(100)
    )

    reviewer = Column(
        String(100)
    )

    rating = Column(
        Integer
    )

    comments = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )