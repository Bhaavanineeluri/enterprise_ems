from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.search import SearchRequest

from services.search import global_search


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/")
def search(
    data: SearchRequest,
    db: Session = Depends(get_db)
):

    return global_search(
        db,
        data.keyword
    )