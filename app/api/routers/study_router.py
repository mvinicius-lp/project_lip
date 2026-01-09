from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.application.use_cases.get_completed_revisions_usecase import GetCompletedRevisionsUseCase
from app.application.use_cases.get_day_history_usecase import GetDayHistoryUseCase
from app.application.use_cases.get_day_overview_usecase import GetDayOverviewUseCase
from app.application.use_cases.get_day_schedule_usecase import GetDayScheduleUseCase
from app.application.use_cases.get_study_history_complete_usecase import GetStudyHistoryCompleteUseCase
from app.application.use_cases.get_week_overview_usecase import GetWeekOverviewUseCase
from app.application.use_cases.mark_completed_revision_usecase import MarkCompletedRevisionUseCase
from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl
from app.infrastructure.mongodb.revision_repository_impl import RevisionRepositoryImpl
from app.application.use_cases.register_study_usecase import RegisterStudyUseCase
from app.application.use_cases.delete_study_usecase import DeleteStudyUseCase
from app.application.use_cases.update_study_usecase import UpdateStudyUseCase

router = APIRouter(prefix="/study", tags=["Estudos"])

# Método auxiliar para converter o tempo de "1:20" para minutos
def convert_time_to_minutes(tempo_dedicado: str):
    try:
        horas, minutos = map(int, tempo_dedicado.split(":"))
        return horas * 60 + minutos
    except ValueError:
        raise ValueError("Tempo dedicado deve estar no formato 'HH:MM'")

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

#Atualiza um estudo
@router.put("/update")
async def update_study(
    study_id: str,
    disciplina: str = None,
    conteudo: str = None,
    horas: int = None,
    minutos: int = None,
    dificuldade: str = None
):
    study_repo = StudyRepositoryImpl()
    
    study_data = {}

    if disciplina:
        study_data["disciplina"] = disciplina
    if conteudo:
        study_data["conteudo"] = conteudo
    if horas is not None:
        study_data["tempo_horas"] = horas
    if minutos is not None:
        study_data["tempo_minutos"] = minutos
    if dificuldade:
        study_data["dificuldade"] = dificuldade

    usecase = UpdateStudyUseCase(study_repo)

    updated = await usecase.execute(study_id, study_data)

    if updated:
        return {"message": "Estudo atualizado com sucesso"}
    else:
        return {"message": "Falha ao atualizar o estudo"}, 400

#Deleta um estudo
@router.delete("/delete")
async def delete_study(study_id: str):
    usecase = DeleteStudyUseCase(
        StudyRepositoryImpl()
    )

    return await usecase.execute(study_id)

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

# VISÃO DE HOJE/A FAZER HOJE
@router.get("/today")
async def today(user_id: str):
    usecase = GetDayOverviewUseCase(StudyRepositoryImpl(), RevisionRepositoryImpl())
    return await usecase.execute(user_id)

# Endpoint para marcar revisão como realizada
@router.post("/mark_completed")
async def mark_completed(revision_id: str, tempo_dedicado: str):
    tempo_minutos = convert_time_to_minutes(tempo_dedicado)
    usecase = MarkCompletedRevisionUseCase(RevisionRepositoryImpl())
    return await usecase.execute(revision_id, tempo_minutos)

# Endpoint para revisões concluídas
@router.get("/completed")
async def completed_revisions(user_id: str):
    usecase = GetCompletedRevisionsUseCase(
        RevisionRepositoryImpl(), StudyRepositoryImpl()
    )
    return await usecase.execute(user_id)

# Endpoint para deletar uma revisão
@router.delete("/revision/delete")
async def delete_revision(revision_id: str):
    revision_repo = RevisionRepositoryImpl()

    success = await revision_repo.delete(revision_id)

    if success:
        return {"message": "Revisão deletada com sucesso!"}
    else:
        raise HTTPException(status_code=404, detail="Revisão não encontrada")
    
# Endpoint que tras o histórico de estudos completo
@router.get("/history/complete")
async def get_study_history(user_id: str):
    """Retorna o histórico de estudos do usuário, incluindo tempo dedicado, disciplinas e tópicos estudados."""
    
    study_repo = StudyRepositoryImpl()
    revision_repo = RevisionRepositoryImpl()

    usecase = GetStudyHistoryCompleteUseCase(study_repo, revision_repo)

    return await usecase.execute(user_id)