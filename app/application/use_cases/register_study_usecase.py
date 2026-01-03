from app.domain.entities.study import Study
from app.domain.entities.revision import Revision

class RegisterStudyUseCase:

    def __init__(self, study_repo, revision_repo):
        self.study_repo = study_repo
        self.revision_repo = revision_repo

    async def execute(self, user_id, disciplina, conteudo, horas, minutos, dificuldade):

        # Criar entidade Study
        study = Study(
            user_id=user_id,
            disciplina=disciplina,
            conteudo=conteudo,
            horas=horas,
            minutos=minutos,
            dificuldade=dificuldade
        )

        # Persistir estudo
        study_created = await self.study_repo.create(study)

        # Gerar revisões com base no comportamento da entidade Study
        datas_revisao = study.gerar_revisoes()

        for data in datas_revisao:
            revision = Revision(
                user_id=user_id,
                study_id=study_created["_id"],
                data_revisao=data
            )
            await self.revision_repo.create(revision)

        return {
            "message": "Estudo registrado com sucesso!",
            "study": study_created
        }
