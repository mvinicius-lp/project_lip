class MarkCompletedRevisionUseCase:
    def __init__(self, revision_repo):
        self.revision_repo = revision_repo

    async def execute(self, revision_id, tempo_dedicado):
        revision = await self.revision_repo.find_by_id(revision_id)
        
        if not revision:
            raise Exception("Revisão não encontrada")

        revision["realizada"] = True
        revision["tempo_dedicado"] = tempo_dedicado  

        await self.revision_repo.update(revision_id, revision)
        
        return {"status": "success", "message": "Revisão marcada como concluída"}
