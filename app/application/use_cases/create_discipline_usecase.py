class CreateDisciplineUseCase:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, user_id: str, nome: str, cor: str):
        return await self.repo.create(user_id, nome, cor)
