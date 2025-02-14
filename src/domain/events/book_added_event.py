from shared.notification import NotificationEvent


class BookAddedEvent(NotificationEvent):
    """Evento disparado quando um livro é adicionado a um autor."""

    def __init__(self, book_title: str, author_name: str):
        """Inicializa o evento com título do livro e nome do autor."""
        super().__init__(message=f"Livro '{book_title}' adicionado ao autor {author_name}", context="BookAdded")
        self.book_title = book_title
        self.author_name = author_name
