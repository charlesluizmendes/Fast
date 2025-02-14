from src.domain.shared.notification import NotificationEvent


class AuthorCreatedEvent(NotificationEvent):
    """Evento disparado quando um autor é criado."""

    def __init__(self, author_name: str):
        """Inicializa o evento com o nome do autor."""
        super().__init__(message=f"Autor {author_name} foi criado", context="AuthorCreated")
        self.author_name = author_name
