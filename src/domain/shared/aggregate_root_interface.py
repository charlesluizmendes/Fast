from abc import ABC

from src.domain.shared.entity import Entity


class AggregateRootInterface(Entity, ABC):
    """Classe base para raízes de agregados."""
    pass