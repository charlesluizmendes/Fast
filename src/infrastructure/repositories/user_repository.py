from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.aggregates.user.user_repository_interface import UserRepositoryInterface
from src.domain.aggregates.user.user import User
from src.infrastructure.models.user_model import UserModel


class UserRepository(UserRepositoryInterface):
    """Implementação do repositório para Usuários usando SQLAlchemy."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find(self, uid: str) -> User:
        """Busca um usuário pelo ID, retornando a instância do modelo ORM."""
        try:
            user = self.db_session.query(UserModel).filter(UserModel.id == uid).first()
            if not user:
                raise Exception(f"Usuário com ID {uid} não encontrado.")
            return user
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")
        
    def find_all(self) -> list[User]:
        """Retorna todos os usuários armazenados."""
        try:
            return self.db_session.query(UserModel).all()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")
        
    def find_by_email(self, email: str) -> User:
        """Retorna o Usuário de acordo com o e-mail."""
        try:
            return self.db_session.query(UserModel).filter(UserModel.email == email).first()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")

    def create(self, user: User) -> None:
        """Adiciona um novo usuário ao banco de dados."""
        try:
            db_user = UserModel(id=user.id, name=user.name, email=user.email, password=user.password)
            self.db_session.add(db_user)
            self.db_session.commit()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, user: User) -> None:
        """Atualiza um usuário existente."""
        try:
            db_user = self.db_session.query(UserModel).filter(UserModel.id == user.id).first()
            if not db_user:
                raise Exception(f"Usuário com ID {user.id} não encontrado.")
            db_user.name = user.name
            db_user.email = user.email
            db_user.password = user.password
            self.db_session.commit()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")

    def delete(self, uid: str) -> None:
        """Remove um usuário pelo ID."""
        try:
            db_user = self.db_session.query(UserModel).filter(UserModel.id == uid).first()
            if not db_user:
                raise Exception(f"Usuário com ID {uid} não encontrado.")
            self.db_session.delete(db_user)
            self.db_session.commit()
        except SQLAlchemyError as e:
            raise Exception(f"Error: {str(e)}")
