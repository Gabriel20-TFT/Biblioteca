from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.book import Book
from models.user import User
from models.loan import Loan
from schemas.loan import LoanRequest, LoanResponse
from datetime import date

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/{book_id}", response_model=LoanResponse, status_code=201)
def borrow(book_id: int, payload: LoanRequest, db: Session = Depends(get_db)):
    # authenticate
    user = db.query(User).filter(User.username == payload.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Authentication failed")
    from utils.security import verify_password
    if not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Authentication failed")

    # check book
    book = db.query(Book).filter(Book.book_id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.available != 1:
        raise HTTPException(status_code=400, detail="Book is not available")

    # create loan and mark book unavailable
    loan = Loan(user_id=user.user_id, book_id=book.book_id, loan_date=date.today())
    try:
        db.add(loan)
        book.available = 0
        db.commit()
        db.refresh(loan)
        return loan
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not create loan")


@router.post("/{book_id}/return", response_model=LoanResponse)
def return_book(book_id: int, payload: LoanRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == payload.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Authentication failed")
    from utils.security import verify_password
    if not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Authentication failed")

    loan = db.query(Loan).filter(Loan.book_id == book_id, Loan.return_date == None).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Active loan not found")
    if loan.user_id != user.user_id:
        raise HTTPException(status_code=403, detail="This loan belongs to another user")

    try:
        loan.return_date = date.today()
        # mark book available
        book = db.query(Book).filter(Book.book_id == book_id).first()
        if book:
            book.available = 1
        db.commit()
        db.refresh(loan)
        return loan
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not return loan")
