from typing import Type, TypeVar, Generic, Optional
from utils.pagination.pagination import paginate
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, obj_id: int):
        return db.query(self.model).filter(
            self.model.id == obj_id
        ).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, obj):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, obj):
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, obj):
        db.delete(obj)
        db.commit()

    def first_by(self, db: Session, **kwargs):
        return db.query(self.model).filter_by(
            **kwargs
        ).first()

    def all_by(self, db: Session, **kwargs):
        return db.query(self.model).filter_by(
            **kwargs
        ).all()

    def exists(self, db: Session, **kwargs):
        return (
            db.query(self.model)
            .filter_by(**kwargs)
            .first()
            is not None
        )
    def paginate_all(
        self,
        db,
        page=1,
        limit=10
    ):

        query = db.query(
        self.model
        )

        return paginate(
        query,
        page,
        limit
    )