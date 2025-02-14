from domain.events.book_added_event import BookAddedEvent


class BookAddedHandler:
    """Handler responsável por processar o evento BookAddedEvent."""

    @staticmethod
    def handle(event: BookAddedEvent):
        """Processa o evento de adição de livro a um autor."""
        print(f"Evento: {event.message}")
