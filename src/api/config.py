import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Config:
    """Configurações da aplicação, carregando do .env."""
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

config = Config()