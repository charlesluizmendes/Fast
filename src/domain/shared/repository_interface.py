from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')


class RepositoryInterface(ABC, Generic[T]):
    """Interface genérica para repositórios no DDD."""

    @abstractmethod
    def find(self, uid: str) -> T:
        """Busca uma entidade pelo ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Retorna todas as entidades do repositório."""
        pass

    @abstractmethod
    def create(self, entity: T) -> None:
        """Adiciona uma nova entidade ao repositório."""
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        """Atualiza uma entidade existente no repositório."""
        pass

    @abstractmethod
    def delete(self, uid: str) -> None:
        """Remove uma entidade pelo ID."""
        pass
