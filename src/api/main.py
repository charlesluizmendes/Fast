from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.application.errorHandlers.error_handler import error_handler
from src.api.routes.author_routes import router as author_router 
from src.api.routes.book_routes import router as book_router
from src.api.routes.user_routes import router as user_router


app = FastAPI(title="Author and Books API", version="1.0")

app.middleware("http")(error_handler)

app.include_router(author_router)
app.include_router(book_router)
app.include_router(user_router)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")