from fastapi import APIRouter, Depends
from application.services.book_service import BookService
from application.dtos.book_dto import BookCreateDTO, BookResponseDTO
from api.dependencies import get_book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponseDTO)
def create_book(book: BookCreateDTO, service: BookService = Depends(get_book_service)):
    return service.create_book(book)
