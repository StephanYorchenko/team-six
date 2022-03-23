from typing import Optional

from core.users.application.repository import IUserRepository
from infrastructure.database.tables import users
from infrastructure.repositories.users.models import User


class PostgresUsersRepository(IUserRepository):
    def __init__(self, database=None):
        self.database = database

    async def get_by_id(self, user_id: str) -> Optional[User]:
        query = users.select().where(users.c.id == user_id)
        # result = await self.database.fetch_one(query)
        return User(
            id=123,
        )
