from pydantic import BaseModel
from typing import Optional
from datetime import date

class LoanRequest(BaseModel):
    username: str
    password: str

class LoanResponse(BaseModel):
    loan_id: int
    user_id: int
    book_id: int
    loan_date: date
    return_date: Optional[date] = None
    class Config:
        from_attribute = True
