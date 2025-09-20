from pydantic import BaseModel
from typing import Optional
from datetime import date

class Loan(BaseModel):
    id: int
    book_id: int
    user_id: int
    loan_date: date
    return_date: Optional[date] = None

class LoanRequest(BaseModel):
    user: str
    password: str
