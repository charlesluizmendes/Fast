from typing import List

from src.domain.shared.aggregate_root_interface import AggregateRootInterface
from src.domain.aggregates.author.book import Book
from src.domain.exceptions.domain_exception import DomainException


class Author(AggregateRootInterface):
    """Representa um autor, raiz do agregado."""

    def __init__(self, uid: str, name: str, books: List[Book] = None):
        """Inicializa o autor com um ID e nome."""
        if not uid.strip():
            raise DomainException("O id do autor não pode estar vazio.")

        if not name.strip():
            raise DomainException("O nome do autor não pode estar vazio.")

        super().__init__(uid)
        self.name = name
        self.books = []
        self.books = books if books is not None else []

        # Disparar evento de criação do autor
        self.add_domain_event(f"Autor {self.name} criado", "AuthorCreated")