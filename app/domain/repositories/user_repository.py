from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    async def create(self, user: User) -> dict:
        pass

    @abstractmethod
    async def delete_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[dict]:
        pass
