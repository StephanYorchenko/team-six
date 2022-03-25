from typing import List, Optional, Dict

from pydantic import BaseModel

from core.partners.application.repository import IPartnersRepository
from core.payments.application.repository import IPaymentRepository
from core.payments.domain.models import Payment


class PaymentInputDTO(BaseModel):
    crm_id: int


class PaymentOutputDTO(Payment):
    identifier: str
    title: str
    description: Optional[str]
    createdAt: str
    amount: float
    logoUrl: Optional[str]
    processed: bool = False
    partner: Dict[str, str]


class GetAllPayments:
    def __init__(self, payments_repository: IPaymentRepository, partners_repository: IPartnersRepository):
        self.payments_repository = payments_repository
        self.partners_repository = partners_repository

    async def execute(self, input_dto: PaymentInputDTO) -> List[PaymentOutputDTO]:
        payments = await self.payments_repository.get_all_by_crm_id(crm_id=input_dto.crm_id)
        result = []
        # Сори за говнокод. Если успею - перепишу
        for payment in payments:
            partner = await self.partners_repository.get_partner_by_identifier(identifier=payment.partnerId)
            result.append(
                PaymentOutputDTO(
                    **payment.dict(),
                    identifier=payment.id,
                    partner={
                        "logoUrl": partner.logoUrl
                    },
                    createdAt=payment.created_at,
                )
            )
        return result
