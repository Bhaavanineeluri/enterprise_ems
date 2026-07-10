from repositories.base import BaseRepository

from models.performance_review import PerformanceReview


performance_review_repository = BaseRepository(
    PerformanceReview
)