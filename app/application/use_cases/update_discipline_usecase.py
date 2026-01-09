class UpdateDisciplineUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, discipline_id: str, data: dict) -> bool:
        return await self.repo.update(discipline_id, data)
