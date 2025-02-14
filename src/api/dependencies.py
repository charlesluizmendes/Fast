from fastapi import Depends
from src.infrastructure.database.database_context import DatabaseContext
from src.infrastructure.repositories.author_repository import AuthorRepository
from src.infrastructure.repositories.book_repository import BookRepository
from src.application.services.author_service import AuthorService
from src.application.services.book_service import BookService

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
