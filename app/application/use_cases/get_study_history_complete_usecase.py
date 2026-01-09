from typing import List
from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl
from app.infrastructure.mongodb.revision_repository_impl import RevisionRepositoryImpl

class GetStudyHistoryCompleteUseCase:
    def __init__(self, study_repo: StudyRepositoryImpl, revision_repo: RevisionRepositoryImpl):
        self.study_repo = study_repo
        self.revision_repo = revision_repo

    async def execute(self, user_id: str) -> List[dict]:
        """Recupera o histórico de estudos de um usuário, incluindo tempo dedicado e tópicos estudados"""
        
        studies = await self.study_repo.find_by_user_id(user_id)

        history = []
        for study in studies:
            revisions = await self.revision_repo.find_by_study_id(study["_id"])

            history.append({
                "data": study["criado_em"],  
                "disciplina": study["disciplina"],  
                "topico_estudado": study["conteudo"],  
                "tempo": f'{study["tempo_horas"]}h {study["tempo_minutos"]}m'  
            })

        return history

