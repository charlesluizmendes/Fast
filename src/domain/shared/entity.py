from src.domain.shared.event.event_interface import EventInterface
from src.domain.shared.event.dispatcher.event_dispatcher import EventDispatcher


class Entity:
    _dispatcher = EventDispatcher()

    def __init__(self, uid: str):
        self._id: str = uid
        self._events: list[EventInterface] = []

    @property
    def id(self) -> str:
        return self._id

    def add_domain_event(self, event: EventInterface) -> None:
        """Adiciona um evento de domínio à entidade e notifica o despachante."""
        self._events.append(event)
        self._dispatcher.notify(event)

    @property
    def domain_events(self) -> list[EventInterface]:
        """Retorna os eventos de domínio registrados na entidade."""
        return self._events

    def clear_domain_events(self) -> None:
        """Remove todos os eventos registrados."""
        self._events.clear()