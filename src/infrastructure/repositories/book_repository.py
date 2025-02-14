from sqlalchemy.orm import Session
from src.domain.aggregates.author.book_repository_interface import BookRepositoryInterface
from src.infrastructure.models.book_model import BookModel


class BookRepository(BookRepositoryInterface):
    """Implementação do repositório para Livros usando SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find(self, uid: str) -> BookModel:
        """Busca um livro pelo ID, retornando a instância do modelo ORM."""
        book = self.db_session.query(BookModel).filter(BookModel.id == uid).first()
        if not book:
            raise Exception(f"Livro com ID {uid} não encontrado.")
        return book  # Retorna a instância do modelo diretamente

    def find_all(self) -> list[BookModel]:
        """Retorna todos os livros armazenados."""
        return self.db_session.query(BookModel).all()

    def create(self, book: BookModel) -> None:
        """Adiciona um novo livro ao banco de dados."""
        self.db_session.add(book)
        self.db_session.commit()

    def update(self, book: BookModel) -> None:
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
