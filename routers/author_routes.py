from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.author import Author
from schemas.author import AuthorCreate, AuthorResponse
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/", response_model=list[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

@router.post("/add", response_model=AuthorResponse, status_code=201)
def add_author(a: AuthorCreate, db: Session = Depends(get_db)):
    author = Author(name=a.name)
    try:
        db.add(author)
        db.commit()
        db.refresh(author)
        return author
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Author already exists")


@router.get("/search", response_model=list[AuthorResponse])
def search_author(name: str, db: Session = Depends(get_db)):
    res = db.query(Author).filter(Author.name.ilike(f"%{name}%")).all()
    if not res:
        raise HTTPException(status_code=404, detail="Author not found")
    return res
