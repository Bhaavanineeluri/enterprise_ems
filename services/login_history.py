from sqlalchemy.orm import Session

from models.login_history import LoginHistory


def create_login_history(
    db: Session,
    user_id: int | None,
    ip_address: str,
    status: str
):

    history = LoginHistory(
        user_id=user_id,
        ip_address=ip_address,
        status=status
    )

    db.add(history)
    db.commit()

    return history