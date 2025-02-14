from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject(ABC):
    """Classe base para Value Objects no DDD."""

    def __eq__(self, other):
        """Verifica se dois Value Objects são iguais pelo seu valor."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __hash__(self):
        """Garante um hashcode baseado nos valores do objeto."""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        """Representação em string do Value Object."""
        return str(self.__dict__)
