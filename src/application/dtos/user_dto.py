from datetime import datetime
from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    """DTO para criação de um Usuário."""
    name: str
    email: str
    password: str


class UserResponseDTO(BaseModel):
    """DTO para resposta contendo dados do Usuário."""
    id: str
    name: str
    email: str


class UserLoginDTO(BaseModel):
    """DTO para login contendo dados do Usuário."""
    email: str
    password: str


class UserLoginResponseDTO(BaseModel):
    """DTO para resposta contendo o Token do Usuário."""
    access_token: str
    expires_at: datetime