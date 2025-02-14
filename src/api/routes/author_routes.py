from fastapi import APIRouter, Depends
from typing import List

from src.application.services.author_service import AuthorService
from src.application.dtos.author_dto import AuthorCreateDTO, AuthorResponseDTO
from src.api.dependencies import get_author_service

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("/", response_model=List[AuthorResponseDTO])
def get_all_authors(service: AuthorService = Depends(get_author_service)):
    return service.get_all_authors()

@router.post("/", response_model=AuthorResponseDTO)
def create_author(author: AuthorCreateDTO, service: AuthorService = Depends(get_author_service)):
    return service.create_author(author)