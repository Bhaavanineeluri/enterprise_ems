from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    total_budget = Column(Float)

    company = relationship("Company")

    items = relationship(
        "BudgetItem",
        back_populates="budget"
    )