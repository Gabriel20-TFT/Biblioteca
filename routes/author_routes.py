from fastapi import APIRouter, HTTPException
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
def search_author(name: str):
    authors = AuthorService.search_authors(name)  # 🔹 aici folosești clasa AuthorService
    if not authors:
        raise HTTPException(status_code=404, detail="Autorul nu a fost găsit")
    return authors
