from app.domain.entities.study import Study
from app.domain.entities.revision import Revision
from app.application.use_cases.update_user_streak_usecase import UpdateUserStreakUseCase
from app.infrastructure.mongodb.user_streak_repository_impl import UserStreakRepositoryImpl

class RegisterStudyUseCase:

    def __init__(self, study_repo, revision_repo):
        self.study_repo = study_repo
        self.revision_repo = revision_repo
        self.streak_usecase = UpdateUserStreakUseCase(
            UserStreakRepositoryImpl()
        )

    async def execute(self, user_id, disciplina, conteudo, horas, minutos, dificuldade):

        study = Study(
            user_id=user_id,
            disciplina=disciplina,
            conteudo=conteudo,
            horas=horas,
            minutos=minutos,
            dificuldade=dificuldade
        )

        study_created = await self.study_repo.create(study)

        datas_revisao = study.gerar_revisoes()

        for data in datas_revisao:
            revision = Revision(
                user_id=user_id,
                study_id=study_created["_id"],
                data_revisao=data
            )
            await self.revision_repo.create(revision)

        current_streak = await self.streak_usecase.execute(user_id)

        return {
            "message": "Estudo registrado com sucesso!",
            "study": study_created,
            "streak": current_streak
        }
