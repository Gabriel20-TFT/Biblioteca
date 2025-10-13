from fastapi import FastAPI
from routers import user_router, author_router, book_router, loan_router, stats_router

app = FastAPI(title="Biblioteca Online")


app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(loan_router)
app.include_router(stats_router)

@app.get("/")
def root():
    return {"message": "Bun venit la Biblioteca Online!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
