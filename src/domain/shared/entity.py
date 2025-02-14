from notification import Notification, NotificationEvent
from event_dispatcher import EventDispatcher


class Entity:
    _dispatcher = EventDispatcher()

    def __init__(self, uid: str):
        self._id: str = uid
        self._notification = Notification()

    @property
    def id(self) -> str:
        return self._id

    @property
    def notification(self) -> Notification:
        """Retorna o gerenciador de notificações da entidade."""
        return self._notification

    def add_domain_event(self, message: str, context: str):
        """Adiciona um evento de domínio e o dispara imediatamente."""
        event = NotificationEvent(message, context)
        self._notification.add_event(event)
        self._dispatcher.dispatch(event)

    def remove_domain_event(self, event: NotificationEvent):
        """Remove um evento específico da lista de notificações."""
        self._notification.remove_event(event)

    def clear_domain_events(self):
        """Remove todos os eventos registrados na entidade."""
        self._notification.clear_events()

    def has_domain_events(self) -> bool:
        """Verifica se a entidade possui eventos de domínio pendentes."""
        return self._notification.has_events()

    def get_domain_events(self) -> list[NotificationEvent]:
        """Retorna a lista de eventos de domínio armazenados."""
        return self._notification.events

    def get_messages_by_context(self, context: str) -> str:
        """Retorna todas as mensagens de um determinado contexto de eventos."""
        return self._notification.messages(context)

    @classmethod
    def register_event_handler(cls, event_type, handler):
        """Registra um handler para um evento específico."""
        cls._dispatcher.register_handler(event_type, handler)
