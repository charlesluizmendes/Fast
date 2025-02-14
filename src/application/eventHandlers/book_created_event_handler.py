from src.domain.shared.event.event_handler_interface import EventHandlerInterface
from src.domain.events.book_created_event import BookCreatedEvent


class BookCreatedEventHandler(EventHandlerInterface):
    """Handler responsável por processar o evento BookCreated."""

    def handle(self, event: BookCreatedEvent) -> None:
        """Processa o evento de criação de autor."""
        print(f"Evento: {event.title} {event.author_id}")
