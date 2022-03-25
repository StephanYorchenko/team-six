from typing import List
from requests import get, post

from core.payments.application.repository import IPaymentRepository
from infrastructure.database.tables import payments
from infrastructure.repositories.payments.models import Payment


class PostgresPaymentsRepository(IPaymentRepository):
    def __init__(self, database):
        self.database = database

    async def get_all_by_crm_id(self, crm_id: str) -> List[Payment]:
        query = payments.select().where(payments.c.crm_id == str(crm_id))
        result = await self.database.fetch_all(query)
        if not result:
            raise Exception()
        return [Payment(**payment) for payment in result]

    async def get_by_id_for_srm(self, crm_id: str, payment_id: str) -> Payment:
        query = payments.select().where(payments.c.crm_id == crm_id and
                                        payments.c.identifier == payment_id)
        result = await self.database.fetch_one(query)
        if not result:
            raise Exception()
        return Payment(**result)


class SandboxAPIPaymentRepository():
    def __init__(self):
        pass

    async def create_payment_consent(self, url: data: Payment, ):
