from sqlalchemy import Column, Integer, String
from database import Base


class PaymentTerm(Base):
    __tablename__ = "payment_terms"

    id = Column(Integer, primary_key=True)

    term_name = Column(String(100))

    due_days = Column(Integer)