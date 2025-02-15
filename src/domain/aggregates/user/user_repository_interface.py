from abc import abstractmethod

from src.domain.shared.repository_interface import RepositoryInterface
from src.domain.aggregates.user.user import User


class UserRepositoryInterface(RepositoryInterface[User]):
    """Interface específica para repositórios de usuários."""

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """Retorna o Usuário de acordo com o e-mail."""
        pass