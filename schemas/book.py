from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author_id: int
    price: Decimal
    available: Optional[int] = 1

class BookResponse(BaseModel):
    book_id: int
    title: str
    author_id: int
    price: Decimal
    available: int
    class Config:
        om_attribute = True
