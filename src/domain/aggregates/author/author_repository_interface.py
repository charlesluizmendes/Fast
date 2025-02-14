from src.domain.shared.repository_interface import RepositoryInterface
from src.domain.aggregates.author.author import Author


class AuthorRepositoryInterface(RepositoryInterface[Author]):
    """Interface específica para repositórios de autores."""
    pass
