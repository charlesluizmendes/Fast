from fastapi import APIRouter, Depends

from src.application.services.user_service import UserService
from src.application.dtos.user_dto import UserCreateDTO, UserResponseDTO, UserLoginDTO, UserLoginResponseDTO
from src.infrastructure.injector_of_dependency import get_user_service


router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/create/", response_model=UserResponseDTO)
async def create_user(user: UserCreateDTO, 
        service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.post("/login/", response_model=UserLoginResponseDTO)
async def login_user(user: UserLoginDTO, 
        service: UserService = Depends(get_user_service)):
    return service.login_user(user)