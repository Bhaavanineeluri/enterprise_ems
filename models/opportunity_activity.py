from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class OpportunityActivity(Base):
    __tablename__ = "opportunity_activities"

    id = Column(Integer, primary_key=True)

    opportunity_id = Column(Integer, ForeignKey("opportunities.id"))

    activity = Column(String(255))

    employee_id = Column(Integer, ForeignKey("employees.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())