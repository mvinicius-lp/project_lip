from datetime import datetime
from fastapi import APIRouter
from app.application.use_cases.get_day_history_usecase import GetDayHistoryUseCase
from app.application.use_cases.get_day_overview_usecase import GetDayOverviewUseCase
from app.application.use_cases.get_day_schedule_usecase import GetDayScheduleUseCase
from app.application.use_cases.get_week_overview_usecase import GetWeekOverviewUseCase
from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl
from app.infrastructure.mongodb.revision_repository_impl import RevisionRepositoryImpl
from app.application.use_cases.register_study_usecase import RegisterStudyUseCase

router = APIRouter(prefix="/study", tags=["Estudos"])

@router.post("/register")
async def register_study(
    user_id: str,
    disciplina: str,
    conteudo: str,
    horas: int,
    minutos: int,
    dificuldade: str
):
    study_repo = StudyRepositoryImpl()
    revision_repo = RevisionRepositoryImpl()
    usecase = RegisterStudyUseCase(study_repo, revision_repo)

    return await usecase.execute(
        user_id=user_id,
        disciplina=disciplina,
        conteudo=conteudo,
        horas=horas,
        minutos=minutos,
        dificuldade=dificuldade
    )

# VISÃO DE HOJE
@router.get("/today")
async def today(user_id: str):
    usecase = GetDayOverviewUseCase(StudyRepositoryImpl(), RevisionRepositoryImpl())
    return await usecase.execute(user_id)

# HISTÓRICO (dia passado)
@router.get("/history")
async def history(user_id: str, date: str):
    date_obj = datetime.fromisoformat(date)
    usecase = GetDayHistoryUseCase(StudyRepositoryImpl(), RevisionRepositoryImpl())
    return await usecase.execute(user_id, date_obj)

# CRONOGRAMA (dia futuro)
@router.get("/schedule")
async def schedule(user_id: str, date: str):
    date_obj = datetime.fromisoformat(date)

    usecase = GetDayScheduleUseCase(
        revision_repo=RevisionRepositoryImpl(),
        study_repo=StudyRepositoryImpl(),
    )

    return await usecase.execute(user_id, date_obj)

# SEMANA ATUAL
@router.get("/week")
async def week(user_id: str):
    usecase = GetWeekOverviewUseCase(StudyRepositoryImpl(), RevisionRepositoryImpl())
    return await usecase.execute(user_id)
