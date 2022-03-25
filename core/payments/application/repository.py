from abc import ABC, abstractmethod
from typing import List

from core.payments.domain.models import Payment


class IPaymentRepository(ABC):
    @abstractmethod
    async def get_all_by_crm_id(self, crm_id: int) -> List[Payment]:
        raise NotImplemented()
