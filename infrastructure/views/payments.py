from typing import List

from fastapi import APIRouter, Body, Depends

from infrastructure.dependencies.auth import get_user_from_token
from infrastructure.dependencies.repositories import get_user_repository

other_routes = APIRouter()


@other_routes.get('/crm/{:crm_id}/payment', response_model=List[PaymentOutputDTO], tags=['Payments'])
async def get_current_user(
        input_dto: PaymentInputDTO = Body(...),
        user=Depends(get_user_from_token),
        payments_repository=Depends(get_payments_repository)
):
    if not user:
        raise Exception()
    use_case = GetPaymentsByUser(payments_repository=payments_repository)
    return await use_case.execute(input_dto=input_dto)
