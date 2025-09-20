from fastapi import APIRouter
from collections import Counter
from services.loan_service import LoanService
from services.book_service import BookService

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/top-books")
def top_books():
    loans = LoanService.get_loans()
    cnt = Counter([l["book_id"] for l in loans])
    top5 = cnt.most_common(5)
    books = BookService.get_books()
    id2title = {b["id"]: b["title"] for b in books}
    result = []
    for book_id, times in top5:
        title = id2title.get(book_id, "(deleted)")
        result.append({"book_id": int(book_id), "title": title, "times": times})
    return result
