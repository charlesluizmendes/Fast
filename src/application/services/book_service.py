import uuid 

from src.application.services.book_service_interface import BookServiceInterface
from src.application.dtos.book_dto import BookCreateDTO, BookResponseDTO
from src.domain.aggregates.author.book import Book 
from src.domain.aggregates.author.book_repository_interface import BookRepositoryInterface
from src.domain.aggregates.author.author_repository_interface import AuthorRepositoryInterface


class BookService(BookServiceInterface):
    """Implementação do serviço de Livros."""

    def __init__(self, book_repository: BookRepositoryInterface, author_repository: AuthorRepositoryInterface):
        """Inicializa o serviço com o repositório injetado."""
        self.book_repository = book_repository
        self.author_repository = author_repository

    def create_book(self, book_dto: BookCreateDTO) -> BookResponseDTO:
        """Cria um novo livro e retorna um DTO de resposta."""
        book_id = str(uuid.uuid4())
        book = Book(uid=book_id, title=book_dto.title, author_id=book_dto.author_id)

        self.book_repository.create(book)
        author = self.author_repository.find(book_dto.author_id)
        return BookResponseDTO(id=book.id, title=book.title, author_name=author.name)