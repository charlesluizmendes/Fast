from domain.events.book_created_event import BookCreatedEvent


class BookCreatedHandler:
    """Handler responsável por processar o evento BookCreated."""

    @staticmethod
    def handle(event: BookCreatedEvent):
        """Processa o evento de criação do livro."""
        print(f"Evento: {event.message}")
