from app.core.database import db
from app.domain.entities.study import Study
from app.domain.repositories.study_repository import StudyRepository

COLLECTION = "studies"

class StudyRepositoryImpl(StudyRepository):

    async def create(self, study: Study):
        study_dict = {
            "user_id": study.user_id,
            "disciplina": study.disciplina,
            "conteudo": study.conteudo,
            "tempo_horas": study.tempo_horas,
            "tempo_minutos": study.tempo_minutos,
            "dificuldade": study.dificuldade,
            "criado_em": study.criado_em
        }

        result = await db[COLLECTION].insert_one(study_dict)
        study_dict["_id"] = str(result.inserted_id)
        return study_dict
