from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from services.search import global_search,autocomplete
from schemas.search import GlobalSearchResponse,AutoCompleteResponse
from services.search import fulltext_search
router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get(
    "",
    response_model=GlobalSearchResponse
)
def search(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    return global_search(db, q)

@router.get("")
def search(
    q: str,
    type: str | None = None,
    db: Session = Depends(get_db)
):
    return global_search(db, q, type)

@router.get(
    "/autocomplete",
    response_model=AutoCompleteResponse
)
def search_autocomplete(
    q: str,
    db: Session = Depends(get_db)
):
    return autocomplete(db, q)
@router.get("/fulltext")
def search_fulltext(
    q: str,
    db: Session = Depends(get_db)
):
    return fulltext_search(
        db,
        q
    )