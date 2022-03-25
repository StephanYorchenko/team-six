from infrastructure.repositories.partners.repository import PostgresPartnersRepository
from infrastructure.repositories.payments.repository import PostgresPaymentsRepository
from infrastructure.database.db import db


def get_payments_repository():
    return PostgresPaymentsRepository(database=db)


def get_partners_repository():
    return PostgresPartnersRepository(database=db)
