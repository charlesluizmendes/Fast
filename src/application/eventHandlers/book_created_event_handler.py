from src.domain.shared.event.event_handler_interface import EventHandlerInterface
from src.domain.events.book_created_event import BookCreatedEvent


class BookCreatedEventHandler(EventHandlerInterface):
    """Handler responsável por processar o evento BookCreatedEvent."""

    def handle(self, event: BookCreatedEvent) -> None:
        """Processa o evento de criação de livro."""
        print(f"Evento: Livro: {event.title} registrado para o Author_Id: {event.author_id}.")
