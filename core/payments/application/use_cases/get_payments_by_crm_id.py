from typing import List

from core.payments.application.repository import IPaymentRepository
from core.payments.domain.models import PaymentInputDTO, PaymentOutputDTO


class GetAllPayments:
    def __init__(self, payments_repository: IPaymentRepository):
        self.payments_repository = payments_repository

    async def execute(self, input_dto: PaymentInputDTO) -> List[PaymentOutputDTO]:
        payments = await self.payments_repository.get_all_by_crm_id(crm_id=input_dto.crm_id)
        return [PaymentOutputDTO(**payment.dict()) for payment in payments]
