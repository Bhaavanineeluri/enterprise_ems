from typing import List, Optional

from pydantic import BaseModel
from typing import List


class SearchItem(BaseModel):
    id: int
    code: Optional[str] = None
    name: str


class GlobalSearchResponse(BaseModel):
    employees: List[SearchItem] = []
    customers: List[SearchItem] = []
    companies: List[SearchItem] = []
    vendors: List[SearchItem] = []
    products: List[SearchItem] = []




class AutoCompleteItem(BaseModel):
    type: str
    id: int
    label: str


class AutoCompleteResponse(BaseModel):
    suggestions: List[AutoCompleteItem]