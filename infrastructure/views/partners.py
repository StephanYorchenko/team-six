from typing import List

from fastapi import APIRouter, Body, Depends

from core.partners.application.use_cases.create_partner import CreatePartnerUseCase, CreatePartnerInputDTO
from core.partners.application.use_cases.get_all_partners import GetAllPartnersUseCase, PartnersListOutDTO
from infrastructure.dependencies.auth import get_user_from_token
from infrastructure.dependencies.repositories import get_partners_repository

partner_routes = APIRouter()


@partner_routes.post('/crm/{crm_id}/partners', response_model=bool, tags=['Partners'])
async def create(
        crm_id: int,
        input_dto: CreatePartnerInputDTO = Body(...),
        partners_repository=Depends(get_partners_repository),
        _=Depends(get_user_from_token),
):
    use_case = CreatePartnerUseCase(partners_repository=partners_repository)
    return await use_case.execute(input_dto=input_dto)


@partner_routes.get('/crm/{crm_id}/partners', response_model=List[PartnersListOutDTO], tags=['Partners'])
async def create(
        crm_id: int,
        partners_repository=Depends(get_partners_repository),
        _=Depends(get_user_from_token),
):
    use_case = GetAllPartnersUseCase(partners_repository=partners_repository)
    return await use_case.execute(crm_id=crm_id)
