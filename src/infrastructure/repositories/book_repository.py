from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.aggregates.author.book_repository_interface import BookRepositoryInterface
from src.domain.aggregates.author.book import Book
from src.infrastructure.models.book_model import BookModel


class BookRepository(BookRepositoryInterface):
    """Implementação do repositório para Livros usando SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find(self, uid: str) -> Book:
        """Busca um livro pelo ID, retornando a instância do modelo ORM."""
        try:
            book = self.db_session.query(BookModel).filter(BookModel.id == uid).first()
            if not book:
                raise Exception(f"Livro com ID {uid} não encontrado.")
            return book  
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")
    
    def find_all(self) -> list[Book]:
        """Retorna todos os livros armazenados."""
        try:
            return self.db_session.query(BookModel).all()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")

    def create(self, book: Book) -> None:
        """Adiciona um novo livro ao banco de dados."""
        try:
            db_book = BookModel(id=book.id, title=book.title, author_id=book.author_id)
            self.db_session.add(db_book)
            self.db_session.commit()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, book: Book) -> None:
        """Atualiza um livro existente."""
        try:
            db_book = self.db_session.query(BookModel).filter(BookModel.id == book.id).first()
            if not db_book:
                raise Exception(f"Livro com ID {book.id} não encontrado.")
            db_book.title = book.title
            self.db_session.commit()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")

    def delete(self, uid: str) -> None:
        """Remove um livro pelo ID."""
        try:
            db_book = self.db_session.query(BookModel).filter(BookModel.id == uid).first()
            if not db_book:
                raise Exception(f"Livro com ID {uid} não encontrado.")
            self.db_session.delete(db_book)
            self.db_session.commit()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")