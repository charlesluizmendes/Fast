from abc import ABC
from entity import Entity


class AggregateRootInterface(Entity, ABC):
    """Classe base para raízes de agregados no DDD."""
    pass
