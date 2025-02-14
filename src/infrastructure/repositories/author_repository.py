from sqlalchemy.orm import Session

from domain.aggregates.author.author import Author
from domain.aggregates.author.author_repository_interface import AuthorRepositoryInterface
from infrastructure.models.author_model import AuthorModel


class AuthorRepository(AuthorRepositoryInterface):
    """Implementação do repositório para Autores usando SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find(self, uid: str) -> Author:
        """Busca um autor pelo ID."""
        author = self.db_session.query(AuthorModel).filter(AuthorModel.id == uid).first()
        if not author:
            raise Exception(f"Autor com ID {uid} não encontrado.")
        return Author(uid=author.id, name=author.name)

    def find_all(self) -> list[Author]:
        """Retorna todos os autores armazenados."""
        authors = self.db_session.query(AuthorModel).all()
        return [Author(uid=a.id, name=a.name) for a in authors]

    def create(self, author: Author) -> None:
        """Adiciona um novo autor ao banco de dados."""
        db_author = AuthorModel(id=author.id, name=author.name)
        self.db_session.add(db_author)
        self.db_session.commit()

    def update(self, author: Author) -> None:
        """Atualiza um autor existente."""
        db_author = self.db_session.query(AuthorModel).filter(AuthorModel.id == author.id).first()
        if not db_author:
            raise Exception(f"Autor com ID {author.id} não encontrado.")
        db_author.name = author.name
        self.db_session.commit()

    def delete(self, uid: str) -> None:
        """Remove um autor pelo ID."""
        db_author = self.db_session.query(AuthorModel).filter(AuthorModel.id == uid).first()
        if not db_author:
            raise Exception(f"Autor com ID {uid} não encontrado.")
        self.db_session.delete(db_author)
        self.db_session.commit()
