from src.domain.shared.repository_interface import RepositoryInterface
from src.domain.aggregates.author.book import Book


class BookRepositoryInterface(RepositoryInterface[Book]):
    """Interface específica para repositórios de livros."""
    pass
