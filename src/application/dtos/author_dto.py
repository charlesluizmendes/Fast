from pydantic import BaseModel
from typing import List


class AuthorCreateDTO(BaseModel):
    """DTO para criação de um autor."""
    name: str


class AuthorResponseDTO(BaseModel):
    """DTO para resposta contendo dados do autor."""
    id: str
    name: str
    books: List[str]  # Lista com os títulos dos livros do autor


class AuthorAddBookDTO(BaseModel):
    """DTO para adicionar um livro ao autor."""
    book_id: str
