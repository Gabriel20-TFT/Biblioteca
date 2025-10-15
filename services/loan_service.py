from utils.file_handler import FileHandler
from datetime import date

LOANS_FILE = "data/loans.csv"
BOOKS_FILE = "data/books.csv"

class LoanService:
    @staticmethod
    def get_loans():
        return FileHandler.read_csv(LOANS_FILE)

    @staticmethod
    def add_loan(book_id: int, user_id: int):
        loans = FileHandler.read_csv(LOANS_FILE)
        next_id = 1
        if loans:
            next_id = max(int(l["id"]) for l in loans) + 1
        new_loan = {
            "id": str(next_id),
            "book_id": str(book_id),
            "user_id": str(user_id),
            "loan_date": date.today().isoformat(),
            "return_date": ""
        }
        loans.append(new_loan)
        FileHandler.write_csv(LOANS_FILE, loans, fieldnames=["id","book_id","user_id","loan_date","return_date"])

        books = FileHandler.read_csv(BOOKS_FILE)
        for b in books:
            if int(b.get("id")) == int(book_id):
                b["available"] = "False"
        FileHandler.write_csv(BOOKS_FILE, books, fieldnames=["id","title","author_id","price","available"])
        return new_loan

    @staticmethod
    def return_loan(book_id: int, user_id: int):
        loans = FileHandler.read_csv(LOANS_FILE)
        for l in loans:
            if int(l.get("book_id")) == int(book_id) and l.get("return_date","") == "":
                l["return_date"] = date.today().isoformat()
                FileHandler.write_csv(LOANS_FILE, loans, fieldnames=["id","book_id","user_id","loan_date","return_date"])

                books = FileHandler.read_csv(BOOKS_FILE)
                for b in books:
                    if int(b.get("id")) == int(book_id):
                        b["available"] = "True"
                FileHandler.write_csv(BOOKS_FILE, books, fieldnames=["id","title","author_id","price","available"])
                return l
        return None
