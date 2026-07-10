from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class LeadSource(Base):
    __tablename__ = "lead_sources"

    id = Column(Integer, primary_key=True)

    source_name = Column(String(100), nullable=False)

    is_active = Column(Boolean, default=True)