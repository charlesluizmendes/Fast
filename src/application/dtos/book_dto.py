from pydantic import BaseModel


class BookCreateDTO(BaseModel):
    """DTO para criação de um livro."""
    title: str
    author_id: str


class BookResponseDTO(BaseModel):
    """DTO para resposta contendo dados do livro."""
    id: str
    title: str
    author_name: str  # Nome do autor ao invés do ID
