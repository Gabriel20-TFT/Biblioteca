from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.book import Book
from models.author import Author
from schemas.book import BookCreate, BookResponse
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.post("/add", response_model=BookResponse, status_code=201)
def add_book(b: BookCreate, db: Session = Depends(get_db)):

    author = db.query(Author).filter(Author.author_id == b.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    book = Book(title=b.title, author_id=b.author_id, price=b.price, available=b.available)
    try:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not add book")


@router.get("/search", response_model=list[BookResponse])
def search_books(title: str, db: Session = Depends(get_db)):
    res = db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
    if not res:
        raise HTTPException(status_code=404, detail="No books found")
    return res
