from fastapi import APIRouter, Depends

from src.api.auth import verify_token
from src.application.services.book_service import BookService
from src.application.dtos.book_dto import BookCreateDTO, BookResponseDTO
from src.infrastructure.injector_of_dependency import get_book_service


router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/create", response_model=BookResponseDTO, status_code=201)
async def create_book(book: BookCreateDTO, 
        service: BookService = Depends(get_book_service),
        user: dict = Depends(verify_token)):
    return service.create_book(book)