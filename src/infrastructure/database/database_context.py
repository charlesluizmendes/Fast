from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

Base = declarative_base()

class DatabaseContext:
    """Gerencia a conexão e sessões do banco de dados."""

    def __init__(self, database_url: str = settings.DATABASE_URL):
        """Inicializa o contexto do banco de dados com a URL configurada."""
        self.engine = create_engine(database_url, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        """Cria as tabelas no banco de dados."""
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """Obtém uma nova sessão do banco de dados."""
        return self.SessionLocal()
