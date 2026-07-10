from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True)

    method_name = Column(String(100))

    is_active = Column(Boolean, default=True)