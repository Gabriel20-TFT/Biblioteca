from fastapi import APIRouter, HTTPException
from models.loan import LoanRequest
from services.loan_service import LoanService
from services.user_service import UserService
from services.book_service import BookService

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/{book_id}")
def borrow(book_id: int, payload: LoanRequest):
    user = UserService.authenticate(payload.user, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Authentication failed")
    books = BookService.get_books()
    book = next((b for b in books if int(b.get("id"))==int(book_id)), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.get("available") != "True":
        raise HTTPException(status_code=400, detail="Book is not available")
    return LoanService.add_loan(book_id=int(book_id), user_id=int(user["id"]))

@router.post("/{book_id}/return")
def return_book(book_id: int, payload: LoanRequest):
    user = UserService.authenticate(payload.user, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Authentication failed")
    res = LoanService.return_loan(book_id=int(book_id), user_id=int(user["id"]))
    if not res:
        raise HTTPException(status_code=404, detail="Active loan for this book not found")
    return res
