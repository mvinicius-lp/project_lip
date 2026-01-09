from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl

class UpdateStudyUseCase:
    def __init__(self, study_repo: StudyRepositoryImpl):
        self.study_repo = study_repo

    async def execute(self, study_id: str, study_data: dict):
        # Chama o método de atualização no repositório
        return await self.study_repo.update(study_id, study_data)
