from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CostCenter(Base):
    __tablename__ = "cost_centers"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    center_name = Column(String(150))
    center_code = Column(String(50))

    is_active = Column(Boolean, default=True)

    company = relationship("Company")