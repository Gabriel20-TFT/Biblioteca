from utils.file_handler import FileHandler
from models.author import Author

AUTHORS_FILE = "data/authors.csv"

class AuthorService:
    @staticmethod
    def get_authors():
        return FileHandler.read_csv(AUTHORS_FILE)

    @staticmethod
    def add_author(author: Author):
        authors = FileHandler.read_csv(AUTHORS_FILE)
        authors.append(author.dict())
        FileHandler.write_csv(AUTHORS_FILE, authors, fieldnames=["id","name"])
        return author

    @staticmethod
    def search_authors(name: str):
        authors = FileHandler.read_csv(AUTHORS_FILE)
        return [a for a in authors if name.lower() in a.get("name","{}").lower()]
