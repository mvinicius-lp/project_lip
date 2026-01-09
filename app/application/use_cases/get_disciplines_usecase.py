class GetDisciplinesUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, user_id: str):
        return await self.repo.find_by_user(user_id)
