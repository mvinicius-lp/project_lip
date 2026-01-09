from datetime import date
from app.domain.entities.user_streak import UserStreak
from app.infrastructure.mongodb.user_streak_repository_impl import UserStreakRepositoryImpl

class UpdateUserStreakUseCase:

    def __init__(self, streak_repo: UserStreakRepositoryImpl):
        self.streak_repo = streak_repo

    async def execute(self, user_id: str):
        today = date.today()

        data = await self.streak_repo.find_by_user_id(user_id)

        if not data:
            await self.streak_repo.create(user_id)
            return 1

        streak = UserStreak(
            user_id=user_id,
            current_streak=data["current_streak"],
            last_activity_date=date.fromisoformat(data["last_activity_date"])
        )

        streak.register_activity(today)

        await self.streak_repo.update(
            user_id,
            streak.current_streak,
            streak.last_activity_date
        )

        return streak.current_streak
