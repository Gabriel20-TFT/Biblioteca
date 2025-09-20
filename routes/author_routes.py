from fastapi import APIRouter
from models.author import Author
from services.author_service import AuthorService

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/")
def list_authors():
    return AuthorService.get_authors()

@router.post("/add")
def add_author(author: Author):
    return AuthorService.add_author(author)

@router.get("/search")
def search_authors(name: str):
    return AuthorService.search_authors(name)
