from fastapi import FastAPI
from database import engine, Base
# import models so SQLAlchemy knows them (not creating tables if you've already created them manually)
import models.user as _user
import models.author as _author
import models.book as _book
import models.loan as _loan

from routers.user_routes import router as user_router
from routers.author_routes import router as author_router
from routers.book_routes import router as book_router
from routers.loan_routes import router as loan_router
from routers.stats_routes import router as stats_router

app = FastAPI(title="Biblioteca Online")



app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(loan_router)
app.include_router(stats_router)

@app.get("/", tags=["general"])
def root():
    return {"message": "Bun venit la Biblioteca Online!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
