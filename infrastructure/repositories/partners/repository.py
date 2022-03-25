import uuid
from typing import Optional, List

from pydantic import BaseModel

from core.partners.application.repository import IPartnersRepository
from infrastructure.database.tables import partners


class Partner(BaseModel):
    id: str
    fullName: str
    taxCode: str
    logoUrl: str
    kpp: str


class PostgresPartnersRepository(IPartnersRepository):
    def __init__(self, database):
        self.database = database

    async def get_partner_by_identifier(self, identifier: str) -> Optional[Partner]:
        query = partners.select().where(partners.c.id == identifier)
        result = await self.database.fetch_one(query)
        return Partner(
            id=result.get("id"),
            fullName=result.get("full_name"),
            taxCode=result.get("tax_code"),
            logoUrl=result.get("logo_url"),
            kpp=result.get("kpp"),
        )

    async def create(self, fullName: str, taxCode: str, kpp: str, logoUrl: str) -> bool:
        query = partners.insert().values(
            full_name=fullName,
            tax_code=taxCode,
            kpp=kpp,
            logo_url=logoUrl,
            id=str(uuid.uuid4())
        )
        await self.database.execute(query)
        return True

    async def get_all(self, crm_id: str) -> List[Partner]:
        query = partners.select()
        results = await self.database.fetch_all(query)
        return [Partner(
            id=result.get("id"),
            fullName=result.get("full_name"),
            taxCode=result.get("tax_code"),
            logoUrl=result.get("logo_url"),
            kpp=result.get("kpp"),
        ) for result in results]
