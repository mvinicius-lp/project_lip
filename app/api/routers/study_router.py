from fastapi import APIRouter
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
