from app.application.use_cases.update_user_streak_usecase import UpdateUserStreakUseCase
from app.infrastructure.mongodb.user_streak_repository_impl import UserStreakRepositoryImpl

class MarkCompletedRevisionUseCase:

    def __init__(self, revision_repo):
        self.revision_repo = revision_repo
        self.streak_usecase = UpdateUserStreakUseCase(
            UserStreakRepositoryImpl()
        )

    async def execute(self, revision_id, tempo_dedicado):
        revision = await self.revision_repo.find_by_id(revision_id)

        if not revision:
            raise Exception("Revisão não encontrada")

        revision["realizada"] = True
        revision["tempo_dedicado"] = tempo_dedicado

        await self.revision_repo.update(revision_id, revision)

        current_streak = await self.streak_usecase.execute(revision["user_id"])

        return {
            "status": "success",
            "message": "Revisão marcada como concluída",
            "streak": current_streak
        }
