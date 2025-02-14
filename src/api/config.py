import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações da aplicação, carregando do .env."""
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///default.db")

config = Config()