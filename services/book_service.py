from utils.file_handler import FileHandler
from models.book import Book

BOOKS_FILE = "data/books.csv"

class BookService:
    @staticmethod
    def get_books():
        return FileHandler.read_csv(BOOKS_FILE)

    @staticmethod
    def add_book(book: Book):
        books = FileHandler.read_csv(BOOKS_FILE)
        books.append(book.dict())
        FileHandler.write_csv(BOOKS_FILE, books, fieldnames=["id","title","author_id","price","available"])
        return book

    @staticmethod
    def search_books(title: str = None, author_id: str = None):
        books = FileHandler.read_csv(BOOKS_FILE)
        if title:
            return [b for b in books if title.lower() in b.get("title","{}").lower()]
        if author_id:
            return [b for b in books if b.get("author_id") == str(author_id)]
        return books

    @staticmethod
    def update_book_availability(book_id: int, available: bool):
        books = FileHandler.read_csv(BOOKS_FILE)
        changed = False
        for b in books:
            if int(b.get("id")) == int(book_id):
                b["available"] = "True" if available else "False"
                changed = True
        if changed:
            FileHandler.write_csv(BOOKS_FILE, books, fieldnames=["id","title","author_id","price","available"])
        return changed
