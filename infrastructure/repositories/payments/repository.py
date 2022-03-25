from typing import List

from core.payments.application.repository import IPaymentRepository
from infrastructure.database.tables import payments
from infrastructure.repositories.payments.models import Payment


class PostgresPaymentsRepository(IPaymentRepository):
    def __init__(self, database):
        self.database = database

    async def get_all_by_crm_id(self, crm_id: str) -> List[Payment]:
        query = payments.select().where(payments.c.crm_id == str(crm_id))
        result = await self.database.fetch_all(query)
        return [Payment(**payment) for payment in result]
