from fastapi import APIRouter, Depends
from typing import List

from application.services.author_service import AuthorService
from application.dtos.author_dto import AuthorCreateDTO, AuthorAddBookDTO, AuthorResponseDTO
from api.dependencies import get_author_service

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("/", response_model=List[AuthorResponseDTO])
def get_all_authors(service: AuthorService = Depends(get_author_service)):
    return service.get_all_authors()

@router.post("/", response_model=AuthorResponseDTO)
def create_author(author: AuthorCreateDTO, service: AuthorService = Depends(get_author_service)):
    return service.create_author(author)

@router.post("/{author_id}/add-book")
def add_book_to_author(author_id: str, book: AuthorAddBookDTO, service: AuthorService = Depends(get_author_service)):
    service.add_book_to_author(author_id, book)
    return {"message": f"Livro {book.book_id} adicionado ao autor {author_id}."}
