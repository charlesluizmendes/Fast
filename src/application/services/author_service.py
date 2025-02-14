from typing import List

from application.services.author_service_interface import AuthorServiceInterface
from application.dtos.author_dto import AuthorCreateDTO, AuthorAddBookDTO, AuthorResponseDTO
from application.dtos.book_dto import BookResponseDTO
from domain.aggregates.author.author_repository_interface import AuthorRepositoryInterface
from domain.aggregates.author.book_repository_interface import BookRepositoryInterface


class AuthorService(AuthorServiceInterface):
    """Implementação do serviço de Autores."""

    def __init__(self, author_repository: AuthorRepositoryInterface, book_repository: BookRepositoryInterface):
        """Inicializa o serviço com os repositórios injetados."""
        self.author_repository = author_repository
        self.book_repository = book_repository

    def get_all_authors(self) -> List[AuthorResponseDTO]:
        """Obtém todos os autores e retorna uma lista de DTOs de resposta."""
        authors = self.author_repository.find_all()
        author_dtos = []

        for author in authors:
            books = [BookResponseDTO(id=book.id, title=book.title, author_name=author.name) for book in author.books]
            author_dtos.append(AuthorResponseDTO(id=author.id, name=author.name, books=books))

        return author_dtos

    def create_author(self, author_dto: AuthorCreateDTO) -> AuthorResponseDTO:
        """Cria um novo autor e retorna um DTO de resposta."""
        author = self.author_repository.create(author_dto.name)
        return AuthorResponseDTO(id=author.id, name=author.name, books=[])

    def add_book_to_author(self, author_id: str, book_dto: AuthorAddBookDTO) -> None:
        """Adiciona um livro a um autor existente."""
        author = self.author_repository.find(author_id)
        book = self.book_repository.find(book_dto.book_id)

        if not book:
            raise Exception("Livro não encontrado.")

        author.add_book(book)
        self.author_repository.update(author)