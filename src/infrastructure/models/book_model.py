from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.infrastructure.database.database_context import Base


class BookModel(Base):
    """Modelo ORM para Livros."""
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(String, ForeignKey("authors.id"), nullable=False)
    author = relationship("AuthorModel", back_populates="books")