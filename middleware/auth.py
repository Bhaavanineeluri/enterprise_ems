from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from utils.jwt_handler import SECRET_KEY, ALGORITHM

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials=Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_email = payload.get("sub")

        if not user_email:
            raise HTTPException(
                status_code=401,
                detail="Invalid token payload"
            )

        user = db.query(User).filter(User.email == user_email).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )