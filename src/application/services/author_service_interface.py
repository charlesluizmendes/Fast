from abc import ABC, abstractmethod
from typing import List

from src.application.dtos.author_dto import AuthorCreateDTO, AuthorAddBookDTO, AuthorResponseDTO


class AuthorServiceInterface(ABC):
    """Interface para o serviço de Autores."""

    @abstractmethod
    def create_author(self, author_dto: AuthorCreateDTO) -> AuthorResponseDTO:
        """Cria um novo autor e retorna um DTO de resposta."""
        pass

    @abstractmethod
    def add_book_to_author(self, author_id: str, book_dto: AuthorAddBookDTO) -> None:
        """Adiciona um livro a um autor existente."""
        pass

    @abstractmethod
    def get_all_authors(self) -> List[AuthorResponseDTO]:
        """Obtém todos os autores e retorna uma lista de DTOs de resposta."""
        pass