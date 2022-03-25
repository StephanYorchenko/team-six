from typing import List

from pydantic import BaseModel

from core.partners.application.repository import IPartnersRepository


class PartnersListOutDTO(BaseModel):
    identifier: str
    logoUrl: str
    fullName: str


class GetAllPartnersUseCase:
    def __init__(self, partners_repository: IPartnersRepository):
        self.partners_repository = partners_repository

    async def execute(self, crm_id: str) -> List[PartnersListOutDTO]:
        partners = await self.partners_repository.get_all(crm_id=crm_id)
        return [
            PartnersListOutDTO(
                identifier=partner.id,
                logoUrl=partner.logoUrl,
                fullName=partner.fullName,
            ) for partner in partners
        ]
