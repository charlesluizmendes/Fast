from shared.repository_interface import RepositoryInterface
from author import Author


class AuthorRepositoryInterface(RepositoryInterface[Author]):
    """Interface específica para repositórios de autores."""
    pass
