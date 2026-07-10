from typing import Type, TypeVar, Generic

from sqlalchemy.orm import Session

from utils.pagination.pagination import paginate

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    # =====================================================
    # BASIC CRUD
    # =====================================================

    def get(
        self,
        db: Session,
        obj_id: int
    ):
        return (
            db.query(self.model)
            .filter(self.model.id == obj_id)
            .first()
        )

    def get_all(
        self,
        db: Session
    ):
        return db.query(self.model).all()

    def create(
        self,
        db: Session,
        obj
    ):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(
        self,
        db: Session,
        obj
    ):
        db.commit()
        db.refresh(obj)
        return obj

    def update_fields(
        self,
        db: Session,
        obj,
        data: dict
    ):
        for key, value in data.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)

        return obj

    def delete(
        self,
        db: Session,
        obj
    ):
        db.delete(obj)
        db.commit()

    # =====================================================
    # FILTERS
    # =====================================================

    def first_by(
        self,
        db: Session,
        **kwargs
    ):
        return (
            db.query(self.model)
            .filter_by(**kwargs)
            .first()
        )

    def all_by(
        self,
        db: Session,
        **kwargs
    ):
        return (
            db.query(self.model)
            .filter_by(**kwargs)
            .all()
        )

    def exists(
        self,
        db: Session,
        **kwargs
    ):
        return (
            db.query(self.model)
            .filter_by(**kwargs)
            .first()
            is not None
        )

    def count(
        self,
        db: Session
    ):
        return db.query(self.model).count()

    # =====================================================
    # COMPANY ISOLATION
    # =====================================================

    def get_by_company(
        self,
        db: Session,
        company_id: int
    ):
        return (
            db.query(self.model)
            .filter(
                self.model.company_id == company_id
            )
            .all()
        )

    def get_one_by_company(
        self,
        db: Session,
        obj_id: int,
        company_id: int
    ):
        return (
            db.query(self.model)
            .filter(
                self.model.id == obj_id,
                self.model.company_id == company_id
            )
            .first()
        )

    def first_by_company(
        self,
        db: Session,
        company_id: int,
        **kwargs
    ):
        kwargs["company_id"] = company_id

        return (
            db.query(self.model)
            .filter_by(**kwargs)
            .first()
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        db: Session,
        column,
        keyword: str
    ):
        return (
            db.query(self.model)
            .filter(column.ilike(f"%{keyword}%"))
            .all()
        )

    # =====================================================
    # PAGINATION
    # =====================================================

    def paginate_all(
        self,
        db: Session,
        page: int = 1,
        limit: int = 10
    ):
        query = db.query(self.model)

        return paginate(
            query,
            page,
            limit
        )