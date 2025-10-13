from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import get_db
from models.loan import Loan
from models.book import Book

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/top-books")
def top_books(db: Session = Depends(get_db)):
    res = (db.query(Book.book_id, Book.title, func.count(Loan.loan_id).label("times"))
             .join(Loan, Loan.book_id == Book.book_id)
             .group_by(Book.book_id)
             .order_by(desc("times"))
             .limit(5)
             .all())

    return [{"book_id": r.book_id, "title": r.title, "times": int(r.times)} for r in res]
