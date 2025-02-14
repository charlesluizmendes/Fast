from abc import ABC, abstractmethod
from typing import List

from src.application.dtos.author_dto import AuthorCreateDTO, AuthorResponseDTO


class AuthorServiceInterface(ABC):
    """Interface para o serviço de Autores."""

    @abstractmethod
    def create_author(self, author_dto: AuthorCreateDTO) -> AuthorResponseDTO:
        """Cria um novo autor e retorna um DTO de resposta."""
        pass

    @abstractmethod
    def get_all_authors(self) -> List[AuthorResponseDTO]:
        """Obtém todos os autores e retorna uma lista de DTOs de resposta."""
        pass