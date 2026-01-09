from fastapi import APIRouter, HTTPException

from app.application.use_cases.update_user_streak_usecase import (
    UpdateUserStreakUseCase
)
from app.infrastructure.mongodb.user_streak_repository_impl import (
    UserStreakRepositoryImpl
)

router = APIRouter(prefix="/streak", tags=["Ofensiva"])


@router.get("/")
async def get_streak(user_id: str):
    repo = UserStreakRepositoryImpl()
    data = await repo.find_by_user_id(user_id)

    if not data:
        return {
            "user_id": user_id,
            "current_streak": 0,
            "last_activity_date": None
        }

    return {
        "user_id": data["user_id"],
        "current_streak": data["current_streak"],
        "last_activity_date": data["last_activity_date"]
    }

