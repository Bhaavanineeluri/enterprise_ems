from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class BudgetItem(Base):
    __tablename__ = "budget_items"

    id = Column(Integer, primary_key=True)

    budget_id = Column(Integer, ForeignKey("budgets.id"))

    category = Column(Integer)

    allocated_amount = Column(Float)

    budget = relationship(
        "Budget",
        back_populates="items"
    )