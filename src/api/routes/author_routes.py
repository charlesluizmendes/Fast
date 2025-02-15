from fastapi import APIRouter, Depends
from typing import List

from src.api.auth import verify_token
from src.application.services.author_service import AuthorService
from src.application.dtos.author_dto import AuthorCreateDTO, AuthorResponseDTO
from src.infrastructure.injector_of_dependency import get_author_service


router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("/", response_model=List[AuthorResponseDTO])
async def get_all_authors(service: AuthorService = Depends(get_author_service), 
        user: dict = Depends(verify_token)):
    return service.get_all_authors()

@router.post("/", response_model=AuthorResponseDTO)
async def create_author(author: AuthorCreateDTO, 
        service: AuthorService = Depends(get_author_service), 
        user: dict = Depends(verify_token)):
    return service.create_author(author)