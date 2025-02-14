from fastapi import Depends
from src.infrastructure.database.database_context import DatabaseContext
from src.infrastructure.repositories.author_repository import AuthorRepository
from src.infrastructure.repositories.book_repository import BookRepository
from src.application.services.author_service import AuthorService
from src.application.services.book_service import BookService

from src.domain.shared.entity import Entity
from src.domain.events.author_created_event import AuthorCreatedEvent
from src.domain.events.book_created_event import BookCreatedEvent
from src.application.eventHandlers.author_created_event_handler import AuthorCreatedHandler
from src.application.eventHandlers.book_created_event_handler import BookCreatedHandler


# Registrar o handler para o evento específico
Entity.register_event_handler(AuthorCreatedEvent, AuthorCreatedHandler.handle)
Entity.register_event_handler(BookCreatedEvent, BookCreatedHandler.handle)

# Criando o banco de dados e sessões
db_context = DatabaseContext()
db_context.create_tables()
session = db_context.get_session()

# Criando os repositórios
def get_author_repo():
    return AuthorRepository(session)

def get_book_repo():
    return BookRepository(session)

# Criando os serviços
def get_author_service(author_repo=Depends(get_author_repo), book_repo=Depends(get_book_repo)):
    return AuthorService(author_repo, book_repo)

def get_book_service(book_repo=Depends(get_book_repo), author_repo=Depends(get_author_repo)):
    return BookService(book_repo, author_repo)
