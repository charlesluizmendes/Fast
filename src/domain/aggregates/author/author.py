from shared.aggregate_root_interface import AggregateRootInterface
from domain.exceptions import DomainException
from book import Book


class Author(AggregateRootInterface):
    """Representa um autor, raiz do agregado."""

    def __init__(self, uid: str, name: str):
        """Inicializa o autor com um ID e nome."""
        if not name.strip():
            raise DomainException("O nome do autor não pode estar vazio.")

        super().__init__(uid)
        self.name = name
        self.books = []

        # Disparar evento de criação do autor
        self.add_domain_event(f"Autor {self.name} criado", "AuthorCreated")

    def add_book(self, book: Book):
        """Adiciona um livro ao autor e dispara um evento."""
        if not isinstance(book, Book):
            raise DomainException("O objeto fornecido não é um livro válido.")

        if any(b.title == book.title for b in self.books):
            raise DomainException(f"O livro '{book.title}' já foi adicionado ao autor {self.name}.")

        self.books.append(book)
        self.add_domain_event(f"Livro '{book.title}' adicionado ao autor {self.name}", "BookAdded")
