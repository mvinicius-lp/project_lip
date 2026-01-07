from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl

class GetCompletedRevisionsUseCase:
    def __init__(self, revision_repo, study_repo: StudyRepositoryImpl):
        self.revision_repo = revision_repo
        self.study_repo = study_repo

    async def execute(self, user_id):
        completed_revisions = await self.revision_repo.find_completed(user_id)

        revisions_with_disciplina = []
        for rev in completed_revisions:
            study_id = rev.get("study_id")
            if study_id:
                study = await self.study_repo.find_by_id(study_id)
                disciplina = study.get("disciplina") if study else "Disciplina não encontrada"
            else:
                disciplina = "Disciplina não encontrada"
            
            rev["disciplina"] = disciplina
            revisions_with_disciplina.append(rev)

        return revisions_with_disciplina
