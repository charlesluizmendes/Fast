from shared.repository_interface import RepositoryInterface
from book import Book


class BookRepositoryInterface(RepositoryInterface[Book]):
    """Interface específica para repositórios de livros."""
    pass
