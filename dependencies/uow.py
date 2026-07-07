from database import get_db
from core.unit_of_work.uow import UnitOfWork


def get_uow(db=next(get_db())):

    return UnitOfWork(db)