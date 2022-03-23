from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: str):
        """docstring"""
        raise NotImplemented()
