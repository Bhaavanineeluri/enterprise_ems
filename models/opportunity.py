from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    title = Column(String(150))

    expected_value = Column(Float)

    stage_id = Column(Integer, ForeignKey("opportunity_stages.id"))

    customer = relationship("Customer")