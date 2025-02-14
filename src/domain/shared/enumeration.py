from enum import Enum


class Enumeration(Enum):
    """Classe base para enumerações no DDD."""

    @classmethod
    def list(cls):
        """Retorna uma lista de tuplas (nome, valor) da enumeração."""
        return list(map(lambda c: (c.name, c.value), cls))

    @classmethod
    def from_value(cls, value):
        """Retorna o membro do enum com base no valor informado."""
        for item in cls:
            if item.value == value:
                return item
        raise ValueError(f"Value '{value}' not found in {cls.__name__}")

    @classmethod
    def values(cls):
        """Retorna uma lista com os valores da enumeração."""
        return [item.value for item in cls]

    @classmethod
    def names(cls):
        """Retorna uma lista com os nomes dos membros da enumeração."""
        return [item.name for item in cls]

    def __str__(self):
        """Retorna o valor do enum como string."""
        return self.value
