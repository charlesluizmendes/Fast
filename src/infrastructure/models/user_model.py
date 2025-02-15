from sqlalchemy import Column, String

from src.infrastructure.database.database_context import Base


class UserModel(Base):
    """Modelo ORM para Usuário."""
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)