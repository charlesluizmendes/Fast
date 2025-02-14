from typing import Union
from fastapi import FastAPI

from src.api.routes.author_routes import router as author_router 
from src.api.routes.book_routes import router as book_router

app = FastAPI(title="Author and Books API", version="1.0")

app.include_router(author_router)
app.include_router(book_router)