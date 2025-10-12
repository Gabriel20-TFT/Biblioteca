from .user_routes import router as user_router
from .author_routes import router as author_router
from .book_routes import router as book_router
from .loan_routes import router as loan_router
from .stats_routes import router as stats_router

__all__ = [
    "user_router",
    "author_router",
    "book_router",
    "loan_router",
    "stats_router"
]