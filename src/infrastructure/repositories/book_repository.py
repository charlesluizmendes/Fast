from sqlalchemy.orm import Session

from src.domain.aggregates.author.book import Book
from src.domain.aggregates.author.book_repository_interface import BookRepositoryInterface
from src.infrastructure.models.book_model import BookModel


class BookRepository(BookRepositoryInterface):
    """Implementação do repositório para Livros usando SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find(self, uid: str) -> Book:
        """Busca um livro pelo ID."""
        book = self.db_session.query(BookModel).filter(BookModel.id == uid).first()
        if not book:
            raise Exception(f"Livro com ID {uid} não encontrado.")
        return Book(uid=book.id, title=book.title, author_id=book.author_id)

    def find_all(self) -> list[Book]:
        """Retorna todos os livros armazenados."""
        books = self.db_session.query(BookModel).all()
        return [Book(uid=b.id, title=b.title, author_id=b.author_id) for b in books]

    def create(self, book: Book) -> None:
        """Adiciona um novo livro ao banco de dados."""
        db_book = BookModel(id=book.id, title=book.title, author_id=book.author_id)
        self.db_session.add(db_book)
        self.db_session.commit()

    def update(self, book: Book) -> None:
        """Atualiza um livro existente."""
        db_book = self.db_session.query(BookModel).filter(BookModel.id == book.id).first()
        if not db_book:
            raise Exception(f"Livro com ID {book.id} não encontrado.")
        db_book.title = book.title
        self.db_session.commit()

    def delete(self, uid: str) -> None:
        """Remove um livro pelo ID."""
        db_book = self.db_session.query(BookModel).filter(BookModel.id == uid).first()
        if not db_book:
            raise Exception(f"Livro com ID {uid} não encontrado.")
        self.db_session.delete(db_book)
        self.db_session.commit()
