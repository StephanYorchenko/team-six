from infrastructure.repositories.payments.repository import PostgresPaymentsRepository
from infrastructure.database.db import db


def get_payments_repository():
    return PostgresPaymentsRepository(database=db)
