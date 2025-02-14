from src.domain.shared.notification import NotificationEvent


class BookCreatedEvent(NotificationEvent):
    """Evento disparado quando um livro é adicionado a um autor."""

    def __init__(self, book_title: str, author_id: str):
        """Inicializa o evento com o nome do livro e o id do autor."""
        super().__init__(message=f"Livro '{book_title}' adicionado ao Autor id {author_id}", context="BookCreated")
        self.book_title = book_title
        self.author_id = author_id
