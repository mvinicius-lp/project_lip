from app.infrastructure.mongodb.user_repository_impl import UserRepositoryImpl

class UpdateUserUseCase:
    def __init__(self, user_repo: UserRepositoryImpl):
        self.user_repo = user_repo

    async def execute(self, user_id: str, name: str):
        return await self.user_repo.update(user_id, name)
