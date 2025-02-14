from typing import Type, Dict, List, Callable
from src.domain.shared.notification import NotificationEvent


class EventDispatcher:
    """Gerenciador central de eventos e handlers."""

    def __init__(self):
        self._handlers: Dict[Type[NotificationEvent], List[Callable[[NotificationEvent], None]]] = {}

    def register_handler(self, event_type: Type[NotificationEvent], handler: Callable[[NotificationEvent], None]):
        """Registra um handler para um evento específico."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def dispatch(self, event: NotificationEvent):
        """Dispara um evento para todos os handlers registrados."""
        event_type = type(event)
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                handler(event)
        else:
            print(f"Nenhum handler registrado para o evento: {event_type.__name__}")
