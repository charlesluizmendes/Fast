from src.domain.events.author_created_event import AuthorCreatedEvent


class AuthorCreatedHandler:
    """Handler responsável por processar o evento AuthorCreatedEvent."""

    @staticmethod
    def handle(event: AuthorCreatedEvent):
        """Processa o evento de criação de autor."""
        print(f"Evento: {event.message}")
