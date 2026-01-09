from fastapi import APIRouter
from app.application.use_cases.get_dashboard_usecase import GetDashboardUseCase
from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl
from app.infrastructure.mongodb.revision_repository_impl import RevisionRepositoryImpl
from app.infrastructure.mongodb.user_streak_repository_impl import UserStreakRepositoryImpl

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
async def get_dashboard(user_id: str):
    usecase = GetDashboardUseCase(
        StudyRepositoryImpl(),
        RevisionRepositoryImpl(),
        UserStreakRepositoryImpl()
    )
    return await usecase.execute(user_id)
