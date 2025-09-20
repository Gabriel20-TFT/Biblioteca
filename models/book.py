from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    price: float
    available: bool = True
