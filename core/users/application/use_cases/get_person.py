from core.users.application.repository import IUserRepository
from core.users.domain.models import UserInputDTO, UserOutputDTO


class GetPersonUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, input_dto: UserInputDTO):
        user = await self.user_repository.get_by_id(user_id=input_dto.identifier)
        return UserOutputDTO(
            login='login1234'
        )
