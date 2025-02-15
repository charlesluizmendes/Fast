from fastapi import APIRouter, Depends

from src.application.services.user_service import UserService
from src.application.dtos.user_dto import UserCreateDTO, UserResponseDTO, UserLoginDTO
from src.api.ioc import get_user_service


router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/create/", response_model=UserResponseDTO)
async def create_user(user: UserCreateDTO, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.post("/login/")
async def login_user(user: UserLoginDTO, service: UserService = Depends(get_user_service)):
    return service.login_user(user)