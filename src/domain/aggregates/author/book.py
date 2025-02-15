from datetime import datetime

from src.domain.shared.entity import Entity
from src.domain.exceptions.domain_exception import DomainException
from src.domain.events.book_created_event import BookCreatedEvent


class Book(Entity):
    """Representa um livro associado a um autor."""

    def __init__(self, uid: str, title: str, author_id: str):
        """Inicializa o livro com um ID, título e ID do autor."""
        
        if not title.strip():
            raise DomainException("O título do livro não pode estar vazio.")

        if not author_id.strip():
            raise DomainException("O ID do autor não pode estar vazio.")

        super().__init__(uid)
        self.title = title
        self.author_id = author_id

        # Disparar evento de criação do livro
        self.add_domain_event(BookCreatedEvent(datetime.now(), self.title, self.author_id))