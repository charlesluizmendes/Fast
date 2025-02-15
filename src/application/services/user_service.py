import uuid 

from src.domain.aggregates.user.user import User
from src.domain.aggregates.user.user_repository_interface import UserRepositoryInterface
from src.application.interfaces.user_service_interface import UserServiceInterface
from src.application.dtos.user_dto import UserCreateDTO, UserResponseDTO, UserLoginDTO, UserLoginResponseDTO
from src.application.utils.user_util import get_password_hash, verify_password, create_access_token


class UserService(UserServiceInterface):
    """Implementação do serviço de Usuário."""

    def __init__(self, user_repository: UserRepositoryInterface):
        """Inicializa o serviço com os repositórios injetados."""
        self.user_repository = user_repository

    def create_user(self, user_dto: UserCreateDTO) -> UserResponseDTO:
        """Cria um novo usuário e retorna um DTO de resposta."""
        user_id = str(uuid.uuid4())
        password_hash = get_password_hash(user_dto.password)
        user = User(uid=user_id, name=user_dto.name, email=user_dto.email, password=password_hash)

        self.user_repository.create(user)
        return UserResponseDTO(id=user.id, name=user.name, email=user.email)
        
    def login_user(self, user_dto: UserLoginDTO) -> UserLoginResponseDTO:
        """Verifica se o usuário é válidos."""
        user = self.user_repository.find_by_email(user_dto.email)

        if user is None or not verify_password(user_dto.password, user.password):
            raise ValueError("Usuário inválido")
        
        access_token, expires_at = create_access_token(
            data={"user": user.email}
        )
        return UserLoginResponseDTO(access_token=access_token, expires_at=expires_at)