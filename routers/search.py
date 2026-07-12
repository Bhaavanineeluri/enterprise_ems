from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db

from dependencies.auth import get_current_user
from dependencies.permissions import require_permission

from schemas.search import (
    GlobalSearchResponse,
    AutoCompleteResponse
)

from services.search import (
    global_search,
    autocomplete,
    fulltext_search
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


# =====================================================
# GLOBAL SEARCH
# =====================================================

@router.get(
    "",
    response_model=GlobalSearchResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("search", "view"))
    ]
)
def search(
    q: str = Query(..., min_length=1),
    type: str | None = None,
    db: Session = Depends(get_db)
):
    return global_search(
        db,
        q,
        type
    )


# =====================================================
# AUTOCOMPLETE
# =====================================================

@router.get(
    "/autocomplete",
    response_model=AutoCompleteResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("search", "view"))
    ]
)
def search_autocomplete(
    q: str,
    db: Session = Depends(get_db)
):
    return autocomplete(
        db,
        q
    )


# =====================================================
# FULL-TEXT SEARCH
# =====================================================

@router.get(
    "/fulltext",
    dependencies=[
        Depends(get_current_user),
        Depends(require_permission("search", "view"))
    ]
)
def search_fulltext(
    q: str,
    db: Session = Depends(get_db)
):
    return fulltext_search(
        db,
        q
    )