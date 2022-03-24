from infrastructure.repositories.users.repository import PostgresUsersRepository


def get_user_repository():
    return PostgresUsersRepository()
