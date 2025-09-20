from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.book_routes import router as book_router
from routes.author_routes import router as author_router
from routes.loan_routes import router as loan_router
from routes.stats_routes import router as stats_router

app = FastAPI(title="Biblioteca Online")
app.include_router(user_router)
app.include_router(book_router)
app.include_router(author_router)
app.include_router(loan_router)
app.include_router(stats_router)
@app.get("/" ,tags=["General"])
def root():
    return {"Bun venit la Biblioteca Online!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)