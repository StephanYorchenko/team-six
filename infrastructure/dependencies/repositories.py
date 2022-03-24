from infrastructure.repositories.payments.repository import PostgresUsersRepository


def get_payments_repository():
    return PostgresPaymentsRepository()
