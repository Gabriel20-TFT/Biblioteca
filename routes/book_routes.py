from fastapi import APIRouter, HTTPException
from models.book import Book
from services.book_service import BookService
from services.author_service import AuthorService

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/")
def list_books():
    return BookService.get_books()

@router.post("/add")
def add_book(book: Book):
    books = BookService.get_books()
    if any(int(b["id"])==book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this id already exists")
    authors = AuthorService.get_authors()
    if not any(int(a["id"])==book.author_id for a in authors):
        raise HTTPException(status_code=400, detail="Author_id does not exist")
    return BookService.add_book(book)

@router.get("/search")
def search_books(title: str = None, author_name: str = None):
    books = BookService.get_books()
    if title:
        return [b for b in books if title.lower() in b.get("title","{}").lower()]
    if author_name:
        authors = AuthorService.get_authors()
        matching = [a for a in authors if author_name.lower() in a.get("name","{}").lower()]
        if not matching:
            return []
        author_ids = {str(a["id"]) for a in matching}
        return [b for b in books if b.get("author_id") in author_ids]
    return books
