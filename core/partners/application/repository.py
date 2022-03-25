from abc import abstractmethod, ABC
from typing import Optional, List

from core.partners.domain.models import Partner


class IPartnersRepository(ABC):
    @abstractmethod
    async def get_partner_by_identifier(self, identifier: str) -> Optional[Partner]:
        ...

    @abstractmethod
    async def create(self, fullName: str, taxCode: str, kpp: str, logoUrl: str) -> bool:
        ...

    @abstractmethod
    async def get_all(self, crm_id: str) -> List[Partner]:
        ...