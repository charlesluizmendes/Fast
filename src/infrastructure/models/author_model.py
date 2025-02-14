from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.infrastructure.database.database_context import Base


class AuthorModel(Base):
    """Modelo ORM para Autores."""
    __tablename__ = "authors"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship("BookModel", back_populates="author")