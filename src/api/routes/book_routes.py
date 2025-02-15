from fastapi import APIRouter, Depends

from src.application.services.book_service import BookService
from src.application.dtos.book_dto import BookCreateDTO, BookResponseDTO
from src.application.utils.user_util import verify_token
from src.api.ioc import get_book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponseDTO)
async def create_book(book: BookCreateDTO, 
        service: BookService = Depends(get_book_service),
        user: dict = Depends(verify_token)):
    return service.create_book(book)