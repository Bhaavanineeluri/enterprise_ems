from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from database import Base


class OTP(Base):
    __tablename__ = "otp"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))  # ✅ FIXED

    otp_hash = Column(String(255), nullable=False)
    purpose = Column(String(50), nullable=False)  # LOGIN / FORGOT / RESET

    expires_at = Column(DateTime, nullable=False)
    is_used = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)