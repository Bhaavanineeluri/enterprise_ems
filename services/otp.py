import random
import hashlib
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from models.otp import OTP


# ---------------------------
# CONFIG
# ---------------------------
OTP_LENGTH = 6
OTP_EXPIRY_MINUTES = 5


# ---------------------------
# HELPERS
# ---------------------------
def generate_otp() -> str:
    return str(random.randint(10**(OTP_LENGTH - 1), (10**OTP_LENGTH) - 1))


def hash_otp(otp: str) -> str:
    return hashlib.sha256(otp.encode()).hexdigest()


def create_otp(db: Session, user_id: int, purpose: str) -> str:
    otp = generate_otp()
    otp_hash = hash_otp(otp)

    db_otp = OTP(
        user_id=user_id,
        otp_hash=otp_hash,
        purpose=purpose,
        expires_at=datetime.utcnow() + timedelta(minutes=OTP_EXPIRY_MINUTES),
        is_used=False
    )

    db.add(db_otp)
    db.commit()
    db.refresh(db_otp)

    return otp


# ---------------------------
# VERIFY OTP
# ---------------------------
def verify_otp(db: Session, user_id: int, otp: str, purpose: str):
    otp_hash = hash_otp(otp)

    db_otp = (
        db.query(OTP)
        .filter(
            OTP.user_id == user_id,
            OTP.purpose == purpose,
            OTP.is_used == False
        )
        .order_by(OTP.id.desc())
        .first()
    )

    if not db_otp:
        return False, "OTP not found"

    if db_otp.otp_hash != otp_hash:
        return False, "Invalid OTP"

    if db_otp.expires_at < datetime.utcnow():
        return False, "OTP expired"

    db_otp.is_used = True
    db.commit()

    return True, "OTP verified"


# ---------------------------
# OPTIONAL: INVALIDATE OLD OTPS
# ---------------------------
def invalidate_otps(db: Session, user_id: int, purpose: str):
    db.query(OTP).filter(
        OTP.user_id == user_id,
        OTP.purpose == purpose,
        OTP.is_used == False
    ).update({"is_used": True})

    db.commit()