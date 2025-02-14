from src.domain.shared.event.event_handler_interface import EventHandlerInterface
from src.domain.events.author_created_event import AuthorCreatedEvent


class AuthorCreatedEventHandler(EventHandlerInterface):
    """Handler responsável por processar o evento AuthorCreatedEvent."""

    def handle(self, event: AuthorCreatedEvent) -> None:
        """Processa o evento de criação de autor."""
        print(f"Evento: {event.author_name}")
