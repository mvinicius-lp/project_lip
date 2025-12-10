from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User
from app.core.database import db

COLLECTION = "users_lip"

class UserRepositoryImpl(UserRepository):

    async def create(self, user: User) -> dict:
        await db[COLLECTION].insert_one(user.model_dump())
        return user.model_dump()

    async def delete_by_email(self, email: str) -> bool:
        result = await db[COLLECTION].delete_one({"email": email})
        return result.deleted_count > 0

    async def get_by_email(self, email: str):
        return await db[COLLECTION].find_one({"email": email})
