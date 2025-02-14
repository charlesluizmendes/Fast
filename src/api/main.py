from typing import Union
from fastapi import FastAPI

from api.routes.author_routes import router as author_router 
from api.routes.book_routes import router as book_router

app = FastAPI(title="Book Management API", version="1.0")

app.include_router(author_router)
app.include_router(book_router)

@app.get("/")
def root():
    return {"message": "API FastAPI está rodando com sucesso!"}