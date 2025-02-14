from typing import Dict, List, Type
from src.domain.shared.event.event_dispatcher_interface import EventDispatcherInterface
from src.domain.shared.event.event_handler_interface import EventHandlerInterface
from src.domain.shared.event.event_interface import EventInterface

EventHandlerMappers = Dict[str, List[EventHandlerInterface]]


class EventDispatcher(EventDispatcherInterface):
    _event_handlers: EventHandlerMappers = {}  # 🔥 Handlers globais para todos os eventos

    @classmethod
    def register_event_handler(cls, event_type: Type[EventInterface], event_handler: EventHandlerInterface):
        """Registra um handler para um evento específico."""
        event_name = event_type.__name__

        if event_name not in cls._event_handlers:
            cls._event_handlers[event_name] = []

        cls._event_handlers[event_name].append(event_handler)
        print(f"✅ Handler {event_handler.__class__.__name__} registrado para {event_name}")

    @classmethod
    def register(cls, event_name: str, event_handler: EventHandlerInterface) -> None:
        """Implementação do método abstrato register."""
        cls.register_event_handler(event_name, event_handler)

    def notify(self, event: EventInterface) -> None:
        """Notifica todos os handlers registrados para um evento."""
        event_name = type(event).__name__
        print(f"🔔 Notificando evento: {event_name}")

        if event_name in self._event_handlers:
            for event_handler in self._event_handlers[event_name]:
                print(f"➡️ Chamando handler: {event_handler.__class__.__name__}")
                event_handler.handle(event)
        else:
            print(f"⚠️ Nenhum handler encontrado para o evento: {event_name}")

    @classmethod
    def unregister(cls, event_name: str, event_handler: EventHandlerInterface) -> None:
        """Remove um handler de um evento específico."""
        if event_name in cls._event_handlers:
            cls._event_handlers[event_name].remove(event_handler)

    @classmethod
    def unregister_all(cls) -> None:
        """Remove todos os handlers registrados."""
        cls._event_handlers.clear()
