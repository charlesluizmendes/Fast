from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class NotificationEvent:
    """Representa um evento de notificação de domínio."""
    occurred_on: datetime
    message: str
    context: str

    def __init__(self, message: str, context: str):
        self.occurred_on = datetime.utcnow()
        self.message = message
        self.context = context


class Notification:
    """Gerenciador de notificações e eventos de domínio."""

    def __init__(self):
        self._events: List[NotificationEvent] = []

    @property
    def events(self) -> List[NotificationEvent]:
        """Retorna os eventos de notificação registrados."""
        return self._events.copy()

    def add_event(self, event: NotificationEvent):
        """Adiciona um evento de notificação."""
        self._events.append(event)

    def remove_event(self, event: NotificationEvent):
        """Remove um evento de notificação."""
        if event in self._events:
            self._events.remove(event)

    def clear_events(self):
        """Remove todos os eventos registrados."""
        self._events.clear()

    def has_events(self) -> bool:
        """Retorna True se houver eventos registrados."""
        return len(self._events) > 0

    def messages(self, context: str) -> str:
        """Retorna todas as mensagens de um determinado contexto."""
        return ", ".join(f"{event.context}: {event.message}" for event in self._events if event.context == context)
