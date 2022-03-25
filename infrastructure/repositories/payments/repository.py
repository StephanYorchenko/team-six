import uuid
from datetime import datetime
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
        return [Payment(
            **payment,
            partnerId=payment.get("partner_id"),
        ) for payment in result][::-1]

    async def get_by_identifier(self, identifier: str) -> List[Payment]:
        query = payments.select().where(payments.c.id == str(identifier))
        payment = await self.database.fetch_one(query)
        return Payment(**payment, partnerId=payment.get("partner_id"))

    async def create(
            self, title: str, description: str, partnerId: str, amount: float, crm_id: str
    ) -> bool:
        query = payments.insert().values(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            partner_id=partnerId,
            amount=amount,
            crm_id=str(crm_id),
            created_at=datetime.now().strftime("%d.%m.%Y"),
            processed=False,
        )
        await self.database.execute(query)
        return True

    async def set_processed(self, payment_id: str) -> bool:
        query = payments\
            .update()\
            .where(payments.c.id == payment_id)\
            .values(processed=True)
        await self.database.execute(query)
        return True
