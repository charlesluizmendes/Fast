from fastapi import Depends

from src.application.services.author_service import AuthorService
from src.application.services.book_service import BookService
from src.application.services.user_service import UserService
from src.application.eventHandlers.author_created_event_handler import AuthorCreatedEventHandler
from src.application.eventHandlers.book_created_event_handler import BookCreatedEventHandler
from src.domain.shared.event.dispatcher.event_dispatcher import EventDispatcher
from src.domain.events.author_created_event import AuthorCreatedEvent
from src.domain.events.book_created_event import BookCreatedEvent
from src.infrastructure.database.database_context import DatabaseContext
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.repositories.author_repository import AuthorRepository
from src.infrastructure.repositories.book_repository import BookRepository


# Database

db_context = DatabaseContext()

# Migration

db_context.create_tables()

# Session

session = db_context.get_session()

# Repositories

def get_author_repository():
    return AuthorRepository(session)

def get_book_repository():
    return BookRepository(session)

def get_user_repository():
    return UserRepository(session)

# Services

def get_author_service(author_repository=Depends(get_author_repository), 
        book_repository=Depends(get_book_repository)):
    return AuthorService(author_repository, book_repository)

def get_book_service(book_repository=Depends(get_book_repository), 
        author_repository=Depends(get_author_repository)):
    return BookService(book_repository, author_repository)

def get_user_service(user_repository=Depends(get_user_repository)):
    return UserService(user_repository)

# EventHandlers 

EventDispatcher.register_event_handler(AuthorCreatedEvent, AuthorCreatedEventHandler())
EventDispatcher.register_event_handler(BookCreatedEvent, BookCreatedEventHandler())