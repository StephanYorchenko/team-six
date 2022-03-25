from typing import List

from pydantic import BaseModel

from core.partners.application.repository import IPartnersRepository
from core.payments.application.repository import IPaymentRepository
from core.payments.domain.models import Payment, Partner


class GetPaymentByIdInputDTO(BaseModel):
    identifier: str
    crm_id: str


class GetPaymentByIdOutputDTO(Payment):
    partner: Partner


class GetPaymentById:
    def __init__(self, payments_repository: IPaymentRepository, partners_repository: IPartnersRepository):
        self.payments_repository = payments_repository
        self.partners_repository = partners_repository

    async def execute(self, input_dto: GetPaymentByIdInputDTO) -> GetPaymentByIdOutputDTO:
        payment = await self.payments_repository.get_by_identifier(identifier=input_dto.identifier)
        partner = await self.partners_repository.get_partner_by_identifier(identifier=payment.partnerId)
        return GetPaymentByIdOutputDTO(
            identifier=payment.identifier,
            title=payment.title,
            description=payment.description,
            created_at=payment.created_at,
            amount=payment.amount,
            processed=payment.processed,
            partner=Partner(
                identifier=partner.identifier,
                logoUrl=partner.logoUrl,
                fullName=partner.fullName,
            )
        )
