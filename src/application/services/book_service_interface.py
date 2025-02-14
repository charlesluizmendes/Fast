from abc import ABC, abstractmethod
from application.dtos.book_dto import BookCreateDTO, BookResponseDTO


class BookServiceInterface(ABC):
    """Interface para o serviço de Livros."""

    @abstractmethod
    def create_book(self, book_dto: BookCreateDTO) -> BookResponseDTO:
        """Cria um novo livro e retorna um DTO de resposta."""
        pass
