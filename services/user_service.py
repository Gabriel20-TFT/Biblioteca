from utils.file_handler import FileHandler
from models.user import User

USERS_FILE = "data/users.csv"

class UserService:
    @staticmethod
    def get_users():
        return FileHandler.read_csv(USERS_FILE)

    @staticmethod
    def save_users(users):
        FileHandler.write_csv(USERS_FILE, users, fieldnames=["id","name","password"])

    @staticmethod
    def add_user(user: User):
        users = FileHandler.read_csv(USERS_FILE)
        users.append(user.dict())
        FileHandler.write_csv(USERS_FILE, users, fieldnames=["id","name","password"])
        return user

    @staticmethod
    def authenticate(name: str, password: str):
        users = FileHandler.read_csv(USERS_FILE)
        for u in users:
            if u.get("name") == name and u.get("password") == password:
                return u
        return None

    @staticmethod
    def find_by_name(name: str):
        users = FileHandler.read_csv(USERS_FILE)
        for u in users:
            if u.get("name") == name:
                return u
        return None
