from abc import ABC, abstractmethod

from src.application.dtos.user_dto import UserCreateDTO, UserResponseDTO, UserLoginDTO, UserLoginResponseDTO


class UserServiceInterface(ABC):
    """Interface para o serviço de Usuários."""

    @abstractmethod
    def create_user(self, user_dto: UserCreateDTO) -> UserResponseDTO:
        """Cria um novo usuário e retorna um DTO de resposta."""
        pass

    @abstractmethod
    def login_user(self, user_dto: UserLoginDTO) -> UserLoginResponseDTO:
        """Verifica se o usuário é válidos."""
        pass