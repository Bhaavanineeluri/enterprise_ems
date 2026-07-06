from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)

    vendor_code = Column(String(50), unique=True)
    name = Column(String(150), nullable=False)

    email = Column(String(150))
    phone = Column(String(20))

    created_at = Column(DateTime(timezone=True), server_default=func.now())