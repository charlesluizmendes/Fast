from src.domain.shared.notification import NotificationEvent


class BookCreatedEvent(NotificationEvent):
    """Evento disparado quando um livro é criado."""

    def __init__(self, title: str, author_id: str):
        """Inicializa o evento com o título e id do autor."""
        super().__init__(message=f"Livro {title} do Autor {author_id} criado", context="BookCreated")
        self.title = title
        self.author_id = author_id