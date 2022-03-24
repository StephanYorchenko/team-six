from fastapi import APIRouter, Body, Depends

from core.users.application.use_cases.get_person import GetPersonUseCase
from core.users.domain.models import UserInputDTO, UserOutputDTO
from infrastructure.dependencies.auth import get_user_from_token
from infrastructure.dependencies.repositories import get_user_repository

other_routes = APIRouter()


@other_routes.post('/user', response_model=UserOutputDTO, tags=['Other'])
async def get_current_user(
        input_dto: UserInputDTO = Body(...),
        user=Depends(get_user_from_token),
        user_repository=Depends(get_user_repository)
):
    if not user:
        raise Exception()
    use_case = GetPersonUseCase(user_repository=user_repository)
    return await use_case.execute(input_dto=input_dto)
