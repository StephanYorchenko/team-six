from infrastructure.repositories.payments.repository import PostgresPaymentsRepository


def get_payments_repository():
    return PostgresPaymentsRepository()
