from typing import List

from infrastructure.database.tables import payments
from infrastructure.repositories.payments.models import Payment


class PostgresPaymentsRepository(IPaymentRepository):
    def __init__(self, database=None):
        self.database = database

    async def get_all_for_crm(self, crm_id: str) -> List[Payment]:
        query = payments.select().where(payments.c.crm_id == crm_id)
        result = await self.database.fetch_one(query)
        if not result:
            raise Exception()
        return [Payment(**payment) for payment in result]
