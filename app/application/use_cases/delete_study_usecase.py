from fastapi import HTTPException

class DeleteStudyUseCase:
    def __init__(self, study_repo):
        self.study_repo = study_repo

    async def execute(self, study_id: str):
        deleted = await self.study_repo.delete(study_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Estudo não encontrado"
            )

        return {
            "message": "Estudo e suas revisões deletados com sucesso"
        }

