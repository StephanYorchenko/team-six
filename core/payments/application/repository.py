from abc import ABC, abstractmethod
from typing import List, Optional

from core.payments.domain.models import Payment


class IPaymentRepository(ABC):
    @abstractmethod
    async def get_all_by_crm_id(self, crm_id: int) -> List[Payment]:
        raise NotImplemented()

    @abstractmethod
    async def get_by_identifier(self, identifier: str) -> Optional[Payment]:
        raise NotImplemented()

    @abstractmethod
    async def create(
            self, title: str, description: str, partnerId: str, amount: float, crm_id: str
    ) -> bool:
        raise NotImplemented()
