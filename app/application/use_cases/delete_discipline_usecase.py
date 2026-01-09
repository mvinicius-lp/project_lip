class DeleteDisciplineUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, discipline_id: str) -> bool:
        return await self.repo.delete(discipline_id)
