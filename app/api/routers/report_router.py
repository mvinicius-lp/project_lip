from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.application.use_cases.generate_report_pdf_usecase import GenerateReportPdfUseCase
from app.infrastructure.mongodb.study_repository_impl import StudyRepositoryImpl
from app.infrastructure.mongodb.revision_repository_impl import RevisionRepositoryImpl
from app.infrastructure.mongodb.user_streak_repository_impl import UserStreakRepositoryImpl

router = APIRouter(prefix="/report", tags=["Relatório"])

@router.get("/download")
async def download_report(user_id: str):
    usecase = GenerateReportPdfUseCase(
        StudyRepositoryImpl(),
        RevisionRepositoryImpl(),
        UserStreakRepositoryImpl()
    )

    pdf_buffer = await usecase.execute(user_id)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=relatorio-estudos.pdf"
        }
    )
