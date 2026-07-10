from sqlalchemy import Column, Integer, String, Float
from database import Base


class TaxRate(Base):
    __tablename__ = "tax_rates"

    id = Column(Integer, primary_key=True)

    tax_name = Column(String(100))

    percentage = Column(Float)