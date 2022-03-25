from typing import List

from fastapi import APIRouter, Depends, Body

from core.payments.application.use_cases.create_payment import CreatePaymentUseCase, CreatePaymentInputDTO
from core.payments.application.use_cases.get_payment_by_id import GetPaymentById, GetPaymentByIdInputDTO, \
    GetPaymentByIdOutputDTO
from core.payments.application.use_cases.get_payments_by_crm_id import GetAllPayments, PaymentInputDTO, PaymentOutputDTO
from infrastructure.dependencies.auth import get_user_from_token
from infrastructure.dependencies.repositories import get_payments_repository, get_partners_repository

payment_routes = APIRouter()


@payment_routes.get('/crm/{crm_id}/payments', response_model=List[PaymentOutputDTO], tags=['Payments'])
async def get_all_payments(
        crm_id: int,
        payments_repository=Depends(get_payments_repository),
        partners_repository=Depends(get_partners_repository),
        _=Depends(get_user_from_token),
):
    use_case = GetAllPayments(payments_repository=payments_repository, partners_repository=partners_repository)
    return await use_case.execute(input_dto=PaymentInputDTO(crm_id=crm_id))


@payment_routes.get('/crm/{crm_id}/payments/{payment_id}', response_model=List[GetPaymentByIdOutputDTO], tags=['Payments'])
async def get_payment(
        crm_id: int,
        payment_id: str,
        payments_repository=Depends(get_payments_repository),
        partners_repository=Depends(get_partners_repository),
        _=Depends(get_user_from_token),
):
    use_case = GetPaymentById(payments_repository=payments_repository, partners_repository=partners_repository)
    return await use_case.execute(input_dto=GetPaymentByIdInputDTO(crm_id=crm_id, identifier=payment_id))


@payment_routes.post('/crm/{crm_id}/payments', response_model=bool, tags=['Payments'])
async def create(
        crm_id: int,
        input_dto: CreatePaymentInputDTO=Body(...),
        payments_repository=Depends(get_payments_repository),
        _=Depends(get_user_from_token),
):
    use_case = CreatePaymentUseCase(payments_repository=payments_repository)
    return await use_case.execute(input_dto=input_dto, crm_id=crm_id)

@payment_routes.post('/crm/{crm_id}/payments/{payment_id}', response_model=bool, tags=['Payments'])
async def create(
        crm_id: int,
        payment_id: str,
        payments_repository=Depends(get_payments_repository),
        _=Depends(get_user_from_token),
):
    await payments_repository.set_processed(payment_id=payment_id)
    return True