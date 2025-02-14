from application.services.book_service_interface import BookServiceInterface
from application.dtos.book_dto import BookCreateDTO, BookResponseDTO
from domain.aggregates.author.book_repository_interface import BookRepositoryInterface


class BookService(BookServiceInterface):
    """Implementação do serviço de Livros."""

    def __init__(self, book_repo: BookRepositoryInterface):
        """Inicializa o serviço com o repositório injetado."""
        self.book_repo = book_repo

    def create_book(self, book_dto: BookCreateDTO) -> BookResponseDTO:
        """Cria um novo livro e retorna um DTO de resposta."""
        book = self.book_repo.create(book_dto.title, book_dto.author_id)
        author_name = self.book_repo.get_author_name(book.author_id)
        return BookResponseDTO(id=book.id, title=book.title, author_name=author_name)