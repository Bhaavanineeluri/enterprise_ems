from sqlalchemy import Column, Integer, String
from database import Base


class OpportunityStage(Base):
    __tablename__ = "opportunity_stages"

    id = Column(Integer, primary_key=True)

    stage_name = Column(String(100))

    sequence = Column(Integer)