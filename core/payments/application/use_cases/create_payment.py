import uuid

from pydantic import BaseModel

from core.payments.application.repository import IPaymentRepository


class CreatePaymentInputDTO(BaseModel):
    title: str
    amount: int
    comment: str
    partnerId: str


class CreatePaymentUseCase:
    def __init__(self, payments_repository: IPaymentRepository):
        self.payments_repository = payments_repository

    async def execute(self, input_dto: CreatePaymentInputDTO, crm_id: str) -> bool:
        await self.payments_repository.create(
            crm_id=crm_id,
            title=input_dto.title,
            amount=input_dto.amount,
            description=input_dto.comment,
            partnerId=input_dto.partnerId
        )
        return True
