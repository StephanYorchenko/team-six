from pydantic import BaseModel

from core.partners.application.repository import IPartnersRepository


class CreatePartnerInputDTO(BaseModel):
    fullName: str
    taxCode: str
    kpp: str
    logoUrl: str


class CreatePartnerUseCase:
    def __init__(self, partners_repository: IPartnersRepository):
        self.partners_repository = partners_repository

    async def execute(self, input_dto: CreatePartnerInputDTO) -> bool:
        await self.partners_repository.create(
            fullName=input_dto.fullName, taxCode=input_dto.taxCode, kpp=input_dto.kpp, logoUrl=input_dto.logoUrl
        )
        return True
