from typing import List

from fastapi import APIRouter, Depends

from core.payments.application.use_cases.get_payments_by_crm_id import GetAllPayments
from core.payments.domain.models import PaymentInputDTO, PaymentOutputDTO
from infrastructure.dependencies.auth import get_user_from_token
from infrastructure.dependencies.repositories import get_payments_repository

payment_routes = APIRouter(prefix='/payments', tags=['Payments'])


@payment_routes.get('/crm/{crm_id}/get_all', response_model=List[PaymentOutputDTO])
async def get_all_payments(
        crm_id: int,
        payments_repository=Depends(get_payments_repository),
        _=Depends(get_user_from_token),
):
    use_case = GetAllPayments(payments_repository=payments_repository)
    return await use_case.execute(input_dto=PaymentInputDTO(crm_id=crm_id))
